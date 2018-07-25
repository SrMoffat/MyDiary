#auth_service.py
import datetime

from flask import request

from app.main.model.users import User

def add_user(data):
    """
    CREATE USER using information in payload
    """
    username = data["username"]
    email = data["email"]
    password = data["password"]

    return {
        "username":username,
        "email":email,
        "password":password
        }
