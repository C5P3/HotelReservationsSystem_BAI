from datetime import date

from dataAccess.baseDataAccess import BaseDataAccess

from model.Room import Room
from model.RoomType import RoomType
from model.Hotel import Hotel
from model.Address import Address
from model.Facility import Facility

class RoomAccess(BaseDataAccess):
    def get_all_rooms(self):
        query = "SELECT room_id, hotel_id, room_number, type_id, price_per_night FROM Room"
        rows = self.execute(query, fetch_all=True)
        if rows:
            return [Room(*row) for row in rows]
        return []

    def get_room_by_id(self, room_id):
        query = "SELECT room_id, hotel_id, room_number, type_id, price_per_night FROM Room WHERE room_id = ?"
        row = self.execute(query, (room_id,), fetch_one=True)
        if row:
            return Room(*row)
        return None
    
    def get_all_rooms_with_facilities(self, ):
        query =  """
        SELECT Room.room_id, Room.room_number, Room.price_per_night, Hotel.hotel_id, Hotel.name 
        AS hotel_name, Hotel.stars 
        AS hotel_stars, RoomType.type_id, RoomType.description 
        AS room_type_description, RoomType.max_guests,
        GROUP_CONCAT(Facilities.facility_name, ', ') AS facilities_list
        FROM Room Room
        JOIN Hotel Hotel ON Room.hotel_id = Hotel.hotel_id
        JOIN Room_Type RoomType ON Room.type_id = RoomType.type_id
        LEFT JOIN Room_Facilities RoomFacilities ON Room.room_id = RoomFacilities.room_id
        LEFT JOIN Facilities Facilities ON RoomFacilities.facility_id = Facilities.facility_id
        GROUP BY Room.room_id, Room.room_number, Room.price_per_night, Hotel.hotel_id, Hotel.name, Hotel.stars, RoomType.type_id, RoomType.description, RoomType.max_guests
        ORDER BY Hotel.name, Room.room_number;
        """
        rows = self.fetchall(query)
        return tuple([
            {"room_id": row["room_id"],
                
            "room_number": row["room_number"],
                
            "price_per_night": row["price_per_night"],
                
            "room_type": {
                "type_id": row["type_id"],
                "description": row["room_type_description"],
                "max_guests": row["max_guests"]},
                
            "hotel": {
                "hotel_id": row["hotel_id"],
                "name": row["hotel_name"],
                "stars": row["hotel_stars"]},
            
            "facilities": [f.strip() for f in (row['facilities_list'] or '').split(',') if f.strip()]} for row in rows])

    def find_available_rooms(self, room_id: int, hotel_id: int, check_in_date: date, check_out_date: date):
        params = []
        query = """ 
        SELECT Room.room_id, hotel_id
        FROM Room
        JOIN Booking ON Booking.room_id = Room.room_id
        WHERE Room.room_id
        NOT IN (
        SELECT room_id
        FROM Booking
        WHERE is_cancelled = 0
        AND (Booking.check_in_date < ? AND Booking.check_out_date > ?) 
        OR (Booking.check_in_date >= ? AND Booking.check_in_date < ?) 
        OR (Booking.check_out_date > ? AND Booking.check_out_date <= ?) 
        OR (Booking.check_in_date <= ? AND Booking.check_out_date >= ?)        
        )
        """