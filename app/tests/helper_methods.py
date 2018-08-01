# helper_methods.py
import json

def register_user(self):
    """
    REGISTER user
    """
    return self.client.post(
        'api/v2/auth/signup',
        data=json.dumps(dict(
            email='testuser@gmail.com',
            username='TestUser',
            password='TestUserpass'
        )),
        content_type='application/json'
        )

def login_user(self):
    """LOGIN user
    """
    return self.client.post(
        'api/v2/auth/login',
        data=json.dumps(dict(
            username='TestUser',
            password='TestUserpass'
        )),
        content_type='application/json'
    )