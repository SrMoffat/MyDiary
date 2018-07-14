# entry_service.py
import uuid
import datetime 

from flask import request 
from app.main.model.entries import Entry, mock_db, MockDB


def add_entry(data):
    """
    CREATE an entry
    """
    title = data['title']
    content = data['content']

    new_entry = Entry(title=title,
                        content=content)

    MockDB.entries.append(new_entry) 
    return {
        'status': 'Created!',
        'id' : new_entry.id,
        'title' : new_entry.title,
        'content': new_entry.content        
    } , 201    

