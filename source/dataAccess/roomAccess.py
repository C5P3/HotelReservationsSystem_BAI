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

    def find_available_rooms(self, check_in_date: date, check_out_date: date):
        query = """ 
            SELECT R.room_id, R.hotel_id
            FROM Room R
            WHERE R.room_id 
            NOT IN (
            SELECT B.room_id 
            FROM Booking B
            WHERE B.is_cancelled = 0
            AND (B.check_in_date < '?' AND B.check_out_date > '?')
            );
        """
        params = () 
        
        rows = self.fetchall(query, params)
        
        return [
            {
                "room_id": row["room_id"],
                "hotel_id": row["hotel_id"]
            }
            for row in rows
        ]
        
    def find_available_rooms(self, check_in_date: date, check_out_date: date, city: str = None, room_type_description: str = None, max_guests_needed: int = None):
        params = []
        query = """
            SELECT R.room_id, R.room_number, R.price_per_night, RT.type_id, RT.description 
            AS room_type_description, RT.max_guests, H.hotel_id, H.name 
            AS hotel_name, H.stars 
            AS hotel_stars, A.address_id, A.street, A.city, A.zip_code,
            GROUP_CONCAT(F.facility_name, ', ') 
            AS facilities_list
            FROM Room R
            JOIN Room_Type RT ON R.type_id = RT.type_id
            JOIN Hotel H ON R.hotel_id = H.hotel_id
            JOIN Address A ON H.address_id = A.address_id
            LEFT JOIN Room_Facilities RF ON R.room_id = RF.room_id
            LEFT JOIN Facilities F ON RF.facility_id = F.facility_id
            WHERE R.room_id NOT IN (
                SELECT B.room_id
                FROM Booking B
                WHERE B.is_cancelled = 0
                AND (B.check_in_date < ? AND B.check_out_date > ?)
            )
        """
        
        params.extend([check_out_date, check_in_date])

        filters = []
        if city:
            filters.append("A.city LIKE ?")
            params.append(f'%{city}%') 
        if room_type_description:
            filters.append("RT.description = ?")
            params.append(room_type_description)
        if max_guests_needed is not None:
            filters.append("RT.max_guests >= ?") 
            params.append(max_guests_needed)
        
        if filters:
            query += " AND " + " AND ".join(filters)

        query += """
            GROUP BY R.room_id, R.room_number, R.price_per_night, RT.type_id, RT.description, RT.max_guests,
                H.hotel_id, H.name, H.stars, A.address_id, A.street, A.city, A.zip_code
            ORDER BY H.name, R.room_number;
        """
        
        rows = self.fetchall(query, tuple(params))
        
        return [
            {
                "room_id": row["room_id"],
                "room_number": row["room_number"],
                "price_per_night": row["price_per_night"],
                "room_type": {
                    "type_id": row["type_id"],
                    "description": row["room_type_description"],
                    "max_guests": row["max_guests"]
                },
                "hotel": {
                    "hotel_id": row["hotel_id"],
                    "name": row["hotel_name"],
                    "stars": row["hotel_stars"],
                    "address": {
                        "address_id": row["address_id"],
                        "street": row["street"],
                        "city": row["city"],
                        "zip_code": row["zip_code"]
                    }
                },
                "facilities": [f.strip() for f in (row['facilities_list'] or '').split(',') if f.strip()]
            }
            for row in rows
        ]