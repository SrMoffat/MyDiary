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
            'error':'Invalid input'
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
        'message' : 'Entry added',
        'entry' : new_entry.display_entry_holder()
    }, 201

def get_all_entries():
    """
    FETCH all entries
    """
    entries = [entry for entry in MockDB.entries]
    if not entries:
        return {
            'message' : 'No entries available!'
        }, 404
    return entries, 200

  

