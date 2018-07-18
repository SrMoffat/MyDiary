# entry_service.py
import datetime  

from flask import request 
from app.main.model.entries import Entry, MockDB


def add_entry(data):
    """
    CREATE an entry
    """
    title = data['title']
    content = data['content']

    # Accept only string
    if isinstance(title, (int, float, complex)) or isinstance(content, (int, float, complex)):
        return {
            'error':'Invalid Input!'
        }, 400

    # Reject null values
    if not title or not content:
        return {
            'error' : 'All fields required!'
        }, 400

    # Reject empty string
    elif len(title.split()) == 0 or len(content.split()) == 0:
        return {
            'error':'Invalid input'
        }, 400

    existing_entries = MockDB.get_all_entries()
    if [entry for entry in existing_entries if entry['title']==title]:
        return {
            'error' : 'Entry already exists!'
        }, 409
        
    # Once checks pass, create entry object
    new_entry = Entry(title=title,
                      content=content)

    # Add it to DB
    MockDB.entries.append(new_entry)    

    return {
        'message' : 'Entry Added!',
        'entry' : new_entry.display_entry_holder()
    }, 201

def get_all_entries():
    """
    FETCH all entries
    """
    # Get a list of all entry objects
    entries = [entry for entry in MockDB.entries]
    if not entries:
        return {
            'message' : 'No entries available!'
        }, 404
    return entries, 200

def get_one_entry(entry_id):
    """
    FETCH one entry
    """
    entry = MockDB.get_entry_by_id(entry_id) 
    if not entry:
        return {
            'message' : 'No entry found!'       
        }, 404

    return entry, 200

def modify_entry(entry_id, data):
    """
    MODIFY an entry
    """
    # Get the entry
    entry = MockDB.get_entry_by_id(entry_id)

    # If entry inexistent send message
    if not entry:
        return {
            'error' : 'Entry not found'
        }, 404

    # Get the update payload
    title = data['title']
    content = data['content']

    # Remove existing object
    MockDB.entries.remove(entry)

    # Check if title and content in payload then update 
    if title:
        entry.title = data['title']
    if content:
        entry.content = data['content']
    entry.date_created = datetime.datetime.utcnow()

    # Add modified entry    
    MockDB.entries.append(entry) 

    return {
        'message': 'Successfully updated!',
        'entry' : entry.display_entry_holder()
        }, 200

def remove_entry(entry_id):
    """
    REMOVE an entry
    """
    # Get the entry
    entry = MockDB.get_entry_by_id(entry_id)

    # If entry inexistent send message
    if not entry:
        return {
            'error' : 'Entry not found'
        }, 404
   
    MockDB.entries.remove(entry)

    return {
        'message': 'Successfully deleted!!'
        
        }, 200


  

