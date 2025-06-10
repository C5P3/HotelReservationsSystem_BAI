import sqlite3

from dataAccess.baseDataAccess import BaseDataAccess
from model.RoomType import RoomType

class RoomTypeAccess(BaseDataAccess):

    def __init__(self, db_connection_str = None):
        super().__init__(db_connection_str)

    def add_room_type(self, description, max_guests):
        query = "INSERT INTO Room_Type (description, max_guests) VALUES (?, ?)"
        self.execute(query, (description, max_guests))
        return True

    def update_room_type(self, type_id, description=None, max_guests=None):
        updates = []
        params = []
        if description is not None:
            updates.append("description = ?")
            params.append(description)
        if max_guests is not None:
            updates.append("max_guests = ?")
            params.append(max_guests)
        if not updates:
            return False
        params.append(type_id)
        query = f"UPDATE Room_Type SET {', '.join(updates)} WHERE type_id = ?"
        self.execute(query, tuple(params))
        return True

    def delete_room_type(self, type_id):
        query = "DELETE FROM Room_Type WHERE type_id = ?"
        self.execute(query, (type_id,))
        return True

    def get_room_type_by_id(self, type_id):
        query = "SELECT type_id, description, max_guests FROM Room_Type WHERE type_id = ?"
        row = self.fetchone(query, (type_id,))
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


