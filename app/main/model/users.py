#users.py
from datetime import datetime, timedelta

import uuid
import jwt 

from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

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
        self.password = generate_password_hash(password)

    def create_token(self, user_id):
        """
        JWT TOKEN Factory
        """
        try:
            payload = {"exp":datetime.utcnow() + timedelta(minutes=15),
                        "iat":datetime.utcnow(),
                        "sub":user_id
                        }
            return jwt.encode(payload, current_app.config.get("SECRET_KEY"))
        except Exception as e:
            print({"message":str(e)})

    @staticmethod
    def decode_token(token):
        """
        DECODE JWT TOKEN
        """
        try:
            payload = jwt.decode(token, current_app.config.get("SECRET_KEY")).decode('utf-8')
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            return {"error" : "Token has expired! Log In"}
        except jwt.InvalidTokenError:
            return {"error" : "Token is invalid! Log In"}

    @staticmethod
    def create_user_query(cursor, username, email, password):
        """
        INSERT USER in DB
        """
        sql_query = "INSERT INTO users (name,email,password) VALUES ({},{},{})".format(username, email, password)
        cursor.execute(sql_query)

    @staticmethod
    def query_user_by_name(dict_cursor, username):
        """
        FETCH USER by USERNAME 
        """
        sql_query = "SELECT * FROM users WHERE username = {}".format(username)
        dict_cursor.execute(sql_query)
        user = dict_cursor.fetchone()
        return user

    @staticmethod
    def query_all_users(dict_cursor):
        """
        FETCH ALL USERS
        """
        sql_query = "SELECT * FROM users"
        dict_cursor.execute(sql_query)
        users = dict_cursor.fetchall()
        return users