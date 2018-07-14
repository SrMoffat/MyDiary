#entries.py
import uuid
from datetime import datetime
from flask import current_app, url_for


class Entry(object): 
    __ID = 1

    def __init__(self, title, content): 
        self.id = Entry.__ID
        self.title = title
        self.content = content
        self.date_created = datetime.utcnow()

        Entry.__ID += 1

    def display_entry_holder(self): 
        return {
            'id' :  self.id,
            'title' :  self.title,
            'content' : self.content,
            'posted on' : self.date_created
        }

mock_db = {
    'entries': [] # Entries table
}

class MockDB(object): 
    entries = []

    @classmethod
    def get_entry(cls, id): 
        for entry in cls.entries: 
            if entry.id == id: 
                return entry
            else: 
                return {
                    'error': 'no entry found'
                }

        