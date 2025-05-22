import os
import sqlite3
from dataAccess.baseDataAccess import BaseDataAccess
from model.Hotel import Hotel

class HotelAccess(BaseDataAccess):
    def __init__(self, db_connection_str = None):
        super().__init__(db_connection_str)

    def get_hotel_by_city(self, city: str) -> None: # Ruft alle Hotels in einer bestimmten Stadt ab.

        query = """
        SELECT Hotel.name, hotel.stars, Address.city
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        WHERE Address.city = ?
        """
        params = (city,)
        results = self.fetchall(query, params)

        hotels = []
        for row in results:
            hotel = Hotel(name=row["name"], stars=row["stars"], city=row["city"])
            hotels.append(hotel)

        return hotels

        


        

