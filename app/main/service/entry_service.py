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
    
    return new_entry.display_entry_holder(), 201  

  
def get_all_entries():
    """
    FETCH all entries
    """
    entries = [entry for entry in MockDB.entries]
    return entries,200
