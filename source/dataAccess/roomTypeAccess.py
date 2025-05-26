from dataAccess.baseDataAccess import BaseDataAccess
from model.RoomType import RoomType

class RoomTypeAccess(BaseDataAccess):
    def get_room_type_by_id(self, type_id):
        query = "SELECT type_id, description, max_guests FROM Room_Type WHERE type_id = ?"
        row = self._execute_query(query, (type_id,), fetch_one=True)
        if row:
            return RoomType(*row)
        return None

    def get_all_room_types(self):
        query = "SELECT type_id, description, max_guests FROM Room_Type"
        rows = self._execute_query(query, fetch_all=True)
        if rows:
            return [RoomType(*row) for row in rows]
        return []
    
