#db.py
import psycopg2
import psycopg2.extras as extras

class DatabaseConnection(object):
    """
    The DB Connection Operations
    """
    def __init__(self):    
        self.connection = psycopg2.connect(database="mydiary_db", 
                                            user="postgres", 
                                            password="rootuser",
                                            host="localhost",
                                            port="5432")
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.dict_cursor = self.connection.cursor(cursor_factory=extras.DictCursor)

    def create_tables(self):
        """
        SQL queries
        """
        sql_queries=(
            """
            CREATE TABLE IF NOT EXISTS users (
                ID INT NOT NULL,
                user_id VARCHAR(255) NOT NULL,
                username VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                date_created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (ID)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS entries (
                ID INT NOT NULL,
                owner_id INT NOT NULL,
                title VARCHAR(255) NOT NULL,
                content text NOT NULL,
                date_created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (owner_id)
                    REFERENCES users (ID)
                    ON UPDATE CASCADE ON DELETE CASCADE
            );
            """
        )
        for query in sql_queries:
            self.cursor.execute(query)

if __name__ == "__main__":
    db_connection = DatabaseConnection()
    db_connection.create_tables()
