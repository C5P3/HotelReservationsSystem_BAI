from dataAccess.baseDataAccess import BaseDataAccess
from model.Room import Room

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
        SELECT
        R.room_id,
        R.room_number,
        R.price_per_night,
        H.hotel_id,
        H.name AS hotel_name,
        H.stars AS hotel_stars,
        RT.type_id,
        RT.description AS room_type_description,
        RT.max_guests,
        GROUP_CONCAT(F.facility_name, ', ') AS facilities_list
        FROM Room R
        JOIN Hotel H ON R.hotel_id = H.hotel_id
        JOIN Room_Type RT ON R.type_id = RT.type_id
        LEFT JOIN Room_Facilities RF ON R.room_id = RF.room_id
        LEFT JOIN Facilities F ON RF.facility_id = F.facility_id
        GROUP BY R.room_id, R.room_number, R.price_per_night, H.hotel_id, H.name, H.stars, RT.type_id, RT.description, RT.max_guests
        ORDER BY H.name, R.room_number;
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
