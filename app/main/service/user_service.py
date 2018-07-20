#user_service.py
import uuid 
import datetime 

from app.main.model.entries import MockDB
from app.main.model.users import User

def save_new_user(data):
    """
    CREATE a user
    """
    username = data['username']
    email = data['email']
    password = data['password']
    clearance = data['clearance']
      
    # Accept only string
    if isinstance(username, (int, float, complex)):
        return {
            'error':'Invalid Input!'
        }, 400
    # Reject null values
    if not username or not email:
        return {
            'error' : 'All fields required!'
        }, 400
    # Password
    if not password:
        return {
            'error':'Password cannot be nul'
        }, 422
    # Reject empty string
    elif len(username.split()) == 0 or len(email.split()) == 0:
        return {
            'error':'Invalid input'
        }, 400
    existing_users = MockDB.get_all_users()

    if [user for user in existing_users if user['username']==username]:
        return {
            'error' : 'Username already exists!'
        }, 409 

               
    # Once checks pass, create entry object
    new_user = User(username=username,
                    email=email,
                    password=password)
    if clearance:
        new_user.clearance = clearance
    # Add it to DB
    MockDB.users.append(new_user)

    return {
        'message' : 'Successfully registered!',
        'user' : new_user.display_user_holder()
    }, 201

def get_users():
    """
    FETCH all users
    """
    # Get a list of all user objects
    users = [user for user in MockDB.users]
    if not users:
        return {
            'message' : 'No entries available!'
        }, 404
    return users, 200

def get_one_user(user_id):
    """
    FETCH one user
    """
    user = MockDB.get_user_by_id(user_id) 
    if not user:
        return {
            'message' : 'No user found!'       
        }, 404
    return user, 200

def modify_user(user_id):
    """
    MODIFY a user's clearance
    """
    # Get the user
    user = MockDB.get_user_by_id(user_id)
    # If user inexistent send message
    if not user:
        return {
            'error' : 'User not found'
        }, 404   
    # Remove existing object
    MockDB.users.remove(user)  
    user.date_created = str(datetime.datetime.utcnow())
    user.clearance = 1
    # Add modified entry    
    MockDB.users.append(user) 
    return {
        'message': 'Successfully updated!',
        'entry' : user.display_user_holder()
        }, 200

def remove_user(user_id):
    """
    REMOVE a user
    """
    # Get the user
    user = MockDB.get_user_by_id(user_id)
    # If user inexistent send message
    if not user:
        return {
            'error' : 'Entry not found'
        }, 404   
    MockDB.users.remove(user)
    return {
        'message': 'Successfully deleted!!'        
        }, 200


