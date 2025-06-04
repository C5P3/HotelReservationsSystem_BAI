# Code aus dem RoomAccess
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