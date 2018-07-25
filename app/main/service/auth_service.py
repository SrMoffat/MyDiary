#auth_service.py
import datetime

from flask import request

from app.main.model.users import User
from app.main.model.db import DatabaseConnection

def add_user(data):
    """
    CREATE USER using information in payload
    """
    username = data["username"]
    email = data["email"]
    password = data["password"]

    # Establish DB connection and Set cursor
    conn = DatabaseConnection()
    cursor = conn.cursor 
    dict_cursor = conn.dict_cursor

    # Check if user exists in DB
    new_user = User.query_user_by_name(dict_cursor, username)

    if not new_user:
        User.create_user_query(cursor, username, email, password)
        new_user_candidate = User.query_user_by_name(dict_cursor, username)
        if new_user_candidate:
            return {
                "status":"success!",
                "message":"User registered!",
            }, 201
    return {
        "status":"failed!",
        "message":"Username exists!"
    }, 409

