from datetime import date

from dataAccess.baseDataAccess import BaseDataAccess

from model.Room import Room
from model.RoomType import RoomType
from model.Hotel import Hotel
from model.Address import Address
from model.Facility import Facility

class RoomAccess(BaseDataAccess):
    def add_room(self, room_number, hotel_id, type_id, price_per_night):
        query = """
            INSERT INTO Room (room_number, hotel_id, type_id, price_per_night)
            VALUES (?, ?, ?, ?)
        """
        self.execute(query, (room_number, hotel_id, type_id, price_per_night))
        return True

    def update_room(self, room_id, room_number=None, hotel_id=None, type_id=None, price_per_night=None):
        updates = []
        params = []
        if room_number is not None:
            updates.append("room_number = ?")
            params.append(room_number)
        if hotel_id is not None:
            updates.append("hotel_id = ?")
            params.append(hotel_id)
        if type_id is not None:
            updates.append("type_id = ?")
            params.append(type_id)
        if price_per_night is not None:
            updates.append("price_per_night = ?")
            params.append(price_per_night)
        if not updates:
            return False 
        params.append(room_id)
        query = f"UPDATE Room SET {', '.join(updates)} WHERE room_id = ?"
        self.execute(query, tuple(params))
        return True

    def delete_room(self, room_id):
        query = "DELETE FROM Room WHERE room_id = ?"
        self.execute(query, (room_id,))
        return True
    
    def get_all_rooms(self):
        query = "SELECT room_id, hotel_id, room_number, type_id, price_per_night FROM Room"
        rows = self.execute(query, fetch_all=True)
        if rows:
            return [Room(*row) for row in rows]
        return []
    
    def get_normal_price_per_night(self, room_id: int):
        query = "SELECT price_per_night FROM Room WHERE room_id = ?"
        row = self.room_access.fetchone(query, (room_id,))
        if row:
            return row['price_per_night']
        return None

    # evtl. löschen ?
    def get_room_by_id(self, room_id):
        query = "SELECT room_id, hotel_id, room_number, type_id, price_per_night FROM Room WHERE room_id = ?"
        row = self.execute(query, (room_id,), fetch_one=True)
        if row:
            return Room(*row)
        return None
    
    def get_room_details_by_id(self, room_id: int):
        query = """
            SELECT R.room_id, R.room_number, R.price_per_night,
                   RT.type_id, RT.description AS room_type_description, RT.max_guests,
                   GROUP_CONCAT(F.facility_name, ', ') AS facilities_list
            FROM Room R
            JOIN Room_Type RT ON R.type_id = RT.type_id
            LEFT JOIN Room_Facilities RF ON R.room_id = RF.room_id
            LEFT JOIN Facilities F ON RF.facility_id = F.facility_id
            WHERE R.room_id = ?
            GROUP BY R.room_id
        """
        row = self.fetchone(query, (room_id,))
        if row:
            return {
                "room_id": row["room_id"],
                "room_number": row["room_number"],
                "price_per_night": row["price_per_night"],
                "room_type": {
                    "type_id": row["type_id"],
                    "description": row["room_type_description"],
                    "max_guests": row["max_guests"]
                },
                "facilities": [f.strip() for f in (row['facilities_list'] or '').split(',') if f.strip()]
            }
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

    def find_available_rooms(self, check_in_date, check_out_date, city=None, room_type_description=None, max_guests=None):
        query = """
            SELECT R.room_id, R.room_number, R.price_per_night,
                   RT.type_id, RT.description AS room_type_description, RT.max_guests,
                   H.name AS hotel_name, H.stars AS hotel_stars, A.city AS hotel_city
            FROM Room R
            JOIN Room_Type RT ON R.type_id = RT.type_id
            JOIN Hotel H ON R.hotel_id = H.hotel_id
            JOIN Address A ON H.address_id = A.address_id
            WHERE R.room_id NOT IN (
                SELECT B.room_id
                FROM Booking B
                WHERE B.is_cancelled = 0
                  AND (B.check_in_date < ? AND B.check_out_date > ?)
            )
        """
        params = [check_out_date, check_in_date]

        if city:
            query += " AND A.city = ?"
            params.append(city)
        if room_type_description:
            query += " AND RT.description = ?"
            params.append(room_type_description)
        if max_guests:
            query += " AND RT.max_guests >= ?"
            params.append(max_guests)

        rows = self.fetchall(query, tuple(params))
        
        rooms = []
        for row in rows:
            hotel = Hotel(row["hotel_name"], row["hotel_stars"], row["hotel_city"])
            room_type = RoomType(row["type_id"], row["room_type_description"], row["max_guests"])
            room = Room(row["room_id"], row["room_number"], row["price_per_night"], room_type, hotel)
            rooms.append(room)

        return rooms
    
    
   

