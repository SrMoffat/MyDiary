#users.py
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask import current_app, url_for

CLEARANCE = {
    'user' : 0,
    'admin' : 1    
}

class User(object): 
    """
    User Class (Model)
    """
    def __init__(self, username, email, password, clearance=CLEARANCE['user']):
        """
        Constructor for User
        :default: user
        """
        self.id = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.clearance = clearance
        self.date_created = str(datetime.utcnow())

    def is_admin(self):
        """
        :return: True if admin
        """
        return self.clearance == CLEARANCE['admin']

    def verify_password(self, password):
        """
        Confirm password hashes match
        """
        return check_password_hash(self.password_hash,password)

    def display_user_holder(self):
        """
        :return User
        """
        return {
            'id': self.id,
            'username': self.username,
            'email':self.email,
            'clearance':self.clearance,
            'created at':self.date_created
            }

