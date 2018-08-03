#decorators
import jwt
from functools import wraps

from flask import request

def token_required(f):
    """
    DECORATOR enforcing JWT
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        token=None
        user_id=""
        if "token" in request.headers:
            token = request.headers["token"]
        if not token:
            return {
                "error":"Token is missing!"
            }
        try:
            payload = jwt.decode(token, "SECRET_KEY")
            user_id = str(payload["sub"])
        except jwt.ExpiredSignatureError:
            return {
                "error":"Token expired! Log In"
            }
        except jwt.InvalidTokenError:
            return {
                "error":"Invalid token! Log In"
            }
        return f(user_id, *args, **kwargs)
    return wrap
