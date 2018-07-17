#entries.py
import uuid
from datetime import datetime

class Entry(object): 
    """
    Entry Class (Model)
    """
    
    def __init__(self, title, content): 
        """
        Entry constructor method 
        """
        self.id = str(uuid.uuid4())
        self.title = title
        self.content = content
        self.date_created = datetime.utcnow()

        

    def display_entry_holder(self): 
        """
        : return entry
        """
        return {
            'id' :  self.id,
            'title' :  self.title,
            'content' : self.content,
            'posted on' : str(self.date_created)
        }



class MockDB(object): 
    entries = []

    @classmethod
    def get_entry_by_id(cls, id): 
        for entry in cls.entries: 
            if entry.display_entry_holder()['id'] == id:                     
                return entry
            
    @classmethod
    def get_all_entries(cls):
       
        return [entry.display_entry_holder() for entry in cls.entries]

                
        