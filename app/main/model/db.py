#db.py
import psycopg2
import psycopg2.extras as extras

from pprint import pprint

class DatabaseConnection(object):
    """
    The DB Connection Operations
    """
    def __init__(self):        
        #try:
        self.connection = psycopg2.connect(database="mydiary_test", 
                                            user="postgres", 
                                            password="rootuser",
                                            host="localhost",
                                            port="5432")
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.dict_cursor = self.connection.cursor(cursor_factory=extras.DictCursor)
        # except Exception as e:
        #     pprint(e)

    def create_tables(self):
        """
        SQL queries
        """
        sql_queries=(
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY_KEY,
                username VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            )
            """
        )
        self.cursor.execute(sql_queries)

if __name__ == "__main__":
    db_connection = DatabaseConnection()
    db_connection.create_tables()