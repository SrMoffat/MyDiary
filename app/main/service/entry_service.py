#entry_service.py
import datetime 

from flask import request

from app.main.model.entries import Entry
from app.main.model.db import DatabaseConnection
from app.main.utils.dto import EntryDto

api = EntryDto.api

# Establish DB connection and Set cursor
conn = DatabaseConnection()
cursor = conn.cursor 
dict_cursor = conn.dict_cursor

def add_entry(data, owner):
    """
    CREATE an ENTRY using information in payload
    """
    title = data["title"]
    content = data["content"]
    
    # Check if entry exists in DB
    new_entry = Entry.query_entry_by_title(dict_cursor, title)
    if not new_entry:
        try:
            if not title or not content:
                return {
                    "status":"failed!",
                    "error":"All fields required!",
                }, 400
              
        except (KeyError) as e:
            return {
                "message":str(e)
            }                

        Entry.add_entry_query(cursor, title, content, owner)
        new_entry_candidate = Entry.query_entry_by_title(dict_cursor, title)
        if new_entry_candidate:
            return {
                "status":"success!",
                "message":"Entry added!"
            }, 201
    return {
        "status":"failed!",
        "message":"Entry with same title exists!"
    }, 409

def get_all_entries(owner):
    """
    FECTH ALL ENTRIES belonging to a user
    """
    entries = Entry.query_all_entries(dict_cursor, owner)
    if not entries:
        api.abort(404, "error: No entries exist!")
    return entries, 200

def get_one_entry(entry_id, owner):
    """
    FECTH ONE ENTRY belonging to a user
    """
    entry = Entry.query_entry_by_id(dict_cursor, entry_id)

    if entry is None:
        api.abort(404, "error: Entry with id: {} does not exist!".format(entry_id))    
    return entry

def modify_entry(entry_id, owner, data):
    """
    MODIFY ONE ENTRY belonging to a user
    """
    
    updated_entry = Entry.query_entry_update(dict_cursor, cursor, entry_id, owner, data)
    
    return {
        "message":"Successfully updated entry!",
        "entry": updated_entry
    }, 200

def remove_entry(owner, entry_id):
    """
    REMOVE an Entry belonging to a user
    """
    Entry.query_remove_entry(dict_cursor,cursor,entry_id,owner)
    return {
        "message":"Entry deleted!"
    }, 200




