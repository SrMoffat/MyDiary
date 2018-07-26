#users.py
from datetime import datetime, timedelta

import uuid
import jwt 

from flask import current_app
from werkzeug.security import generate_password_hash

class User(object):
    """
    The USER model for the API
    """
    def __init__(self, id, username, email, password):
        """
        Constructor for a USER
        """
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def create_user_query(cursor, username, email, password):
        """
        INSERT USER in DB
        """
        user_id = str(uuid.uuid4())
        password = generate_password_hash(password)
        sql_query = "INSERT INTO users (user_id,username,email,password) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql_query, (user_id,username, email, password))

    @staticmethod
    def query_user_by_name(dict_cursor, username):
        """
        FETCH USER by USERNAME 
        """
        sql_query = "SELECT * FROM users WHERE username = %s"
        dict_cursor.execute(sql_query,[username])
        user = dict_cursor.fetchone()
        return user

    @staticmethod
    def query_user_password_hash(dict_cursor, username):
        """
        FETCH USER by USERNAME 
        """
        user = User.query_user_by_name(dict_cursor,username)    
        return user["password"]

    @staticmethod
    def query_all_users(dict_cursor):
        """
        FETCH ALL USERS
        """
        sql_query = "SELECT * FROM users"
        dict_cursor.execute(sql_query)
        users = dict_cursor.fetchall()
        return users