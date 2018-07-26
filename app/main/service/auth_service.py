#auth_service.py
import datetime
import re

from flask import request
from werkzeug.security import check_password_hash

from app.main.model.users import User
from app.main.model.db import DatabaseConnection

email_expression = re.compile(
    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
pattern = re.compile(
    r"(^[A-Za-z]+$)")

# Establish DB connection and Set cursor
conn = DatabaseConnection()
cursor = conn.cursor 
dict_cursor = conn.dict_cursor

def add_user(data):
    """
    REGISTER a USER using information in payload
    """
    username = data["username"]
    email = data["email"]
    password = data["password"]

    # Check if user exists in DB
    new_user = User.query_user_by_name(dict_cursor, username)

    if not new_user:
        try:
            if not (re.match(pattern,username)):
                return {
                    "status":"failed!",
                    "error":"Invalid characters in username!",
                }, 400
            if len(password) < 6:
                return {
                    "status":"failed!",
                    "error":"Password too weak!",
                }, 400
            if not (re.match(email_expression,email)):
                return {
                    "status":"failed!",
                    "error":"Invalid email!",
                }, 400
        except (KeyError) as e:
            return {
                "message":str(e)
            }                

        User.create_user_query(cursor, username, email, password)
        new_user_candidate = User.query_user_by_name(dict_cursor, username)
        if new_user_candidate:
            return {
                "status":"success!",
                "message":"User registered!"
            }, 201
    return {
        "status":"failed!",
        "message":"Username exists!"
    }, 409

def login_user(data):
    """
    LOGIN a REGISTERED USER
    """
    username = data["username"]
    password = data["password"]
    

    # Check if user exists in DB
    login_candidate = User.query_user_by_name(dict_cursor, username)
    if login_candidate:
        # Retrieve password hash from DB then compare to password
        if check_password_hash(User.query_user_password_hash(dict_cursor, username), password):
            return {
                "status":"success!",
                "message":"You are now logged in!"
            }, 200
        else:
            return {
                "status":"failed!",
                "message":"Incorrect password!"
            },401 
    else:
        return {
            "status":"failed!",
            "error":"Invalid credentials!"
        },401
     


