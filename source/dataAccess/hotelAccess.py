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
    
    def get_hotel_by_city_and_stars(self, city: str, stars: int) -> list[Hotel]:

        query = """
        SELECT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        WHERE Address.city = ?
        AND Hotel.stars >= ?
        """
        params = (city, stars)
        results = self.fetchall(query, params)

        hotels = []
        for row in results:
            hotel_id, hotel_name, hotel_stars, address_id, address_street, address_city, address_zip = row
            address = Address(address_id, address_street, address_city, address_zip)
            hotel = Hotel(hotel_id, hotel_name, hotel_stars, address)
            hotels.append(hotel)

        return hotels
    
    def get_hotel_by_city_and_max_guests(self, city: str, max_guests: int) -> list[Hotel]:

        query = """
        SELECT DISTINCT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        JOIN Room ON Hotel.hotel_id = Room.hotel_id
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        WHERE Address.city = ?
        AND Room_Type.max_guests >= ?
        """
        params = (city, max_guests)
        results = self.fetchall(query, params)

        hotels = []
        for row in results:
            hotel_id, hotel_name, hotel_stars, address_id, address_street, address_city, address_zip = row
            address = Address(address_id, address_street, address_city, address_zip)
            hotel = Hotel(hotel_id, hotel_name, hotel_stars, address)
            hotels.append(hotel)

        return hotels
    
    def get_hotel_by_city_and_dates(self, city: str, check_in_date: str, check_out_date: str) -> list[Hotel]:

        query = """
        SELECT DISTINCT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        WHERE Address.city = ?
        AND Hotel.hotel_id IN (
            SELECT hotel_id
            FROM available_hotel_rooms
            WHERE city = ?
            AND room_id NOT IN (
                SELECT room_id
                FROM Booking
                WHERE NOT (
                    Booking.check_out_date <= ?
                    OR Booking.check_in_date >= ?
                )
            )
        );
        """
        params = (city, check_in_date, check_out_date)
        results = self.fetchall(query, params)

        hotels = []
        for row in results:
            hotel_id, hotel_name, hotel_stars, address_id, address_street, address_city, address_zip = row
            address = Address(address_id, address_street, address_city, address_zip)
            hotel = Hotel(hotel_id, hotel_name, hotel_stars, address)
            hotels.append(hotel)

        return hotels
    
    def get_hotel_by_combinations(self, city: str, stars: int, max_guests: int, check_in_date: str, check_out_date: str) -> list[Hotel]:

        query = """
        SELECT DISTINCT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        JOIN Room ON Room.hotel_id = Hotel.hotel_id
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        WHERE Address.city = ?
        AND Hotel.stars >= ?
        AND Room_Type.max_guests >= ?
        AND Room.room_id NOT IN (
                SELECT Booking.room_id
                FROM Booking
                WHERE NOT (
                    Booking.check_out_date <= ?
                    OR Booking.check_in_date >= ?
            )
        );
        """
        params = (city, stars, max_guests, check_in_date, check_out_date)
        results = self.fetchall(query, params)

        hotels = []
        for row in results:
            hotel_id, hotel_name, stars, address_id, street, city, zip_code = row
            address = Address(address_id, street, city, zip_code)
            hotel = Hotel(hotel_id, hotel_name, stars, address)
            hotels.append(hotel)

        return hotels
    
    def get_hotel_information(self) -> list[Hotel]:

        query = """
        SELECT Hotel.name, Hotel.stars, Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id;
        """
        results = self.fetchall(query)

        hotels = []
        for row in results:
            hotel_id, hotel_name, stars, address_id, street, zip_code, city = row
            address = Address(address_id, street, city, zip_code)
            hotel = Hotel(hotel_id, hotel_name, stars, address)
            hotels.append(hotel)

        return hotels

    def add_hotel(self, name:str, stars:int, address_id:int):
        query_highest_id = """ SELECT MAX(hotel_id) FROM Hotel """
        result_highest_id = self.fetchone(query_highest_id)
        if result_highest_id is None:
            result_highest_id = 0

        query_add_hotel = """ INSERT INTO Hotel (?, ?, ?, ?) """
        self.execute(query_add_hotel, (result_highest_id + 1, name, stars, address_id))
        return True
    
    def update_hotel(self, hotel_id:int, name:str = None, stars:int = None, address_id:int = None):
        query = " UPDATE hotel SET "
        fields = []
        params = []
        
        if name is not None:
            fields.append("name = ?")
            params.append(name)
        if stars is not None:
            fields.append("stars = ?")
            params.append(stars)
        if address_id is not None:
            fields.append("address_id = ?")
            params.append(address_id)
        
        query += ", ".join(fields)
        query += " WHERE hotel_id = ?"
        params.append(hotel_id)
        
        result = self.execute(query, tuple(params))
        
        if result == 0:
            return False
        else:
            return True
        
    def delete_hotel(self, hotel_id:int):
        query = """ DELETE FROM Hotel WHERE hotel_id = ? """
        row_deleted = self.execute(query, (hotel_id,))
        if row_deleted < 1:
            return False
        else:
            return True
    
    
