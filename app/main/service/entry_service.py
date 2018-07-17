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
    return entries, 200

def get_one_entry(entry_id):
    """
    FETCH an entry
    """
    entry = MockDB.get_entry_by_id(entry_id)
    
    return entry, 200

def modify_entry(entry_id, data):
    entry = MockDB.get_entry_by_id(entry_id)
    entry_data = entry.display_entry_holder()

    entry_data['title'] = data['title']
    entry_data['content'] = data['content']

    return entry_data, 200

    

    


