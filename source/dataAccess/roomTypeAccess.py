import sqlite3

from dataAccess.baseDataAccess import BaseDataAccess
from model.RoomType import RoomType

class RoomTypeAccess(BaseDataAccess):
    def __init__(self, db_connection_str: str):
        super().__init__(db_connection_str)

    def get_room_type_by_id(self, type_id):
        query = "SELECT type_id, description, max_guests FROM Room_Type WHERE type_id = ?"
        row = self.fetchone(query, (type_id,), fetch_one=True)
        if row:
            return RoomType(row['type_id'], row['description'], row['max_guests'])
        return None
    
    def get_room_type_by_description(self, description: str):
        query = "SELECT type_id, description, max_guests FROM Room_Type WHERE description = ?"
        row = self.fetchone(query, (description,))
        if row:
            return RoomType(row['type_id'], row['description'], row['max_guests'])
        return None

    def get_all_room_types(self):
        query = "SELECT type_id, description, max_guests FROM Room_Type"
        rows = self.fetchall(query)
        return [RoomType(row['type_id'], row['description'], row['max_guests']) for row in rows]
    
