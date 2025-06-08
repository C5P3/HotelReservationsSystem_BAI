import os
import sqlite3

from dataAccess.baseDataAccess import BaseDataAccess
from model.Guest import Guest

class GuestAccess:

    def __init__(self, db_connection_str = None):
        super().__init__(db_connection_str)
    
    def get_all_guests(self) -> list[Guest]:
    query = """
    SELECT guest_id, first_name, last_name, email
    FROM Guest
    """
    results = self.fetchall(query)

    guests = []
    for row in results:
        guest_id, first_name, last_name, email = row
        guest = Guest(guest_id, first_name, last_name, email)
        guests.append(guest)

    return guests
