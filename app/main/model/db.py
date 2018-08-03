#db.py
import os
import psycopg2
import psycopg2.extras as extras

class DatabaseConnection(object):
    """
    The DB Connection Operations
    """
    def __init__(self):
        if os.getenv("DB_NAME") is None:
            DATABASE_URI = "postgres://hxvydazlnrmxle:5833dbd808eb14d23ed84175ea265b34dd3dcb352a80bdf952c840e5fe480eaf@ec2-23-23-242-163.compute-1.amazonaws.com:5432/da0b1qovika6ca"  
        else:
            DATABASE_URI = "postgres://postgres:rootuser@localhost/mydiary_db"
        self.connection = psycopg2.connect(database=os.getenv("DB_NAME"), 
                                            user=os.getenv("DB_USER"), 
                                            password=os.getenv("DB_PWD"),
                                            host=os.getenv("DB_HOST"),
                                            port=os.getenv("DB_PORT"))
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
                ID SERIAL,
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
                ID SERIAL,
                owner_id INT NOT NULL,
                title VARCHAR(255) NOT NULL,
                content text NOT NULL,
                date_created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (ID),
                FOREIGN KEY (owner_id)
                    REFERENCES users (ID)
                    ON UPDATE CASCADE ON DELETE CASCADE
            );
            """
        )
        for query in sql_queries:
            self.cursor.execute(query)

    def drop_all(self):
        drop_queries=(
            """
            DROP TABLE IF EXISTS users CASCADE
            """,
            """
            DROP TABLE IF EXISTS entries CASCADE
            """
        )
        for query in drop_queries:
            self.cursor.execute(query)

if __name__ == "__main__":
    db_connection = DatabaseConnection()
    db_connection.create_tables()
