import os
import sqlite3

from dataAccess.baseDataAccess import BaseDataAccess
from model.Address import Address
from model.Hotel import Hotel


class HotelAccess(BaseDataAccess):
    def __init__(self, db_connection_str = None):
        super().__init__(db_connection_str)

    def get_hotel_by_city(self, city: str) -> list[Hotel]: # Ruft alle Hotels in einer bestimmten Stadt ab und gibt sie als Liste von Hotel-Objekten zurück.

        query = """
        SELECT Hotel.hotel_id, Hotel.name, hotel.stars, Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        WHERE Address.city = ?
        """
        params = (city,)
        results = self.fetchall(query, params)

        hotels = []
        for row in results:
            hotel_id, hotel_name, hotel_stars, address_id, address_street, address_city, address_zip = row
            address = Address(address_id, address_street, address_city, address_zip)
            hotel = Hotel(hotel_id, hotel_name, hotel_stars, address)
            hotels.append(hotel)

        return hotels
    
    
    


        


        

