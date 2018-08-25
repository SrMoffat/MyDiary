#db.py
import os
import psycopg2
import psycopg2.extras as extras
from urllib.parse import urlparse

class DatabaseConnection(object):
    """
    The DB Connection Operations
    """
    def __init__(self):
        
        self.connection = self.connect()
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.dict_cursor = self.connection.cursor(cursor_factory=extras.DictCursor)
    
    def connect(self):
        db_uri = os.getenv("DATABASE_URI")
        result = urlparse(db_uri)
        host = result.hostname
        role = result.username
        pwd = result.password
        database = result.path[1:]
        
        return psycopg2.connect(database=database, 
                                user=role, 
                                password=pwd,
                                host="localhost",
                                port="5432")

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
