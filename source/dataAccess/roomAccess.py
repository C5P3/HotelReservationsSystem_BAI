from dataAccess.baseDataAccess import BaseDataAccess
from model.Room import Room

class RoomAccess(BaseDataAccess):
    def get_all_rooms(self):
        query = "SELECT room_id, hotel_id, room_number, type_id, price_per_night FROM Room"
        rows = self._execute_query(query, fetch_all=True)
        if rows:
            return [Room(*row) for row in rows]
        return []

    def get_room_by_id(self, room_id):
        query = "SELECT room_id, hotel_id, room_number, type_id, price_per_night FROM Room WHERE room_id = ?"
        row = self._execute_query(query, (room_id,), fetch_one=True)
        if row:
            return Room(*row)
        return None