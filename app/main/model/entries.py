#entries.py
import jwt
from datetime import datetime

from flask import current_app
from werkzeug.security import generate_password_hash

class Entry(object):
    """
    The ENTRY model for the API
    """
    def __init__(self, id, owner, title, content):
        """
        Constructor for an ENTRY
        """
        self.id = id
        self.author = owner
        self.title = title
        self.content = content

    @staticmethod
    def add_entry_query(cursor, title, content, owner):
        """
        INSERT ENTRY in DB
        """
        sql_query = "INSERT INTO entries (title,content,owner_id) VALUES (%s,%s,%s)"
        cursor.execute(sql_query, (title,content,owner))

    @staticmethod
    def query_entry_by_title(dict_cursor, title):
        """
        FETCH ENTRY by TITLE
        """
        sql_query = "SELECT * FROM entries WHERE title = %s"
        dict_cursor.execute(sql_query,[title])
        entry = dict_cursor.fetchone()        
        return entry

    @staticmethod
    def query_entry_by_id(dict_cursor, entry_id):
        """
        FETCH ENTRY by ID
        """
        sql_query = "SELECT * FROM entries WHERE id = %s"
        dict_cursor.execute(sql_query,([entry_id]))
        entry_data = dict_cursor.fetchone()
        
        entry_holder = {
            "id": entry_data[0],
            "owner":entry_data[1],
            "title": entry_data[2],
            "content": entry_data[3],
            "date created": entry_data[4]
        }
        return entry_holder

    @staticmethod
    def query_all_entries(dict_cursor, user_id):
        """
        FETCH ALL entries 
        """
        sql_query = "SELECT * FROM entries WHERE owner_id = %s"
        dict_cursor.execute(sql_query, (user_id))
        entries = dict_cursor.fetchall()
        entry_holder = []
        for entry in entries:
            entry_result = {
                "id":entry[0],
                "title":entry[2],
                "content":entry[3],
                "owner":entry[1],
                "date created":entry[4].strftime("%d-%b-%Y : %H:%M:%S")
                }
            entry_holder.append(entry_result)
        return entry_holder

    @staticmethod
    def query_entry_update(dict_cursor, cursor, data, entry_id, owner):
        entry = Entry.query_entry_by_id(dict_cursor,entry_id)
        sql_query = "UPDATE entries SET title=%s, content=%s WHERE (id=%s)"
        cursor.execute(sql_query, (owner[u"title"],owner[u"content"],entry_id))
        entry["date created"] = str(entry["date created"])
        return entry

    @staticmethod
    def query_remove_entry(dict_cursor,cursor,entry_id,owner):
        Entry.query_entry_by_id(dict_cursor, entry_id)
        sql_query = "DELETE from entries WHERE (id=%s)"
        cursor.execute(sql_query,[entry_id])
        


    
    