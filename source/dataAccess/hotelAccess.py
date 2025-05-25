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
        params = (city, city, check_in_date, check_out_date)
        results = self.fetchall(query, params)

        hotels = []
        for row in results:
            hotel_id, hotel_name, hotel_stars, address_id, address_street, address_city, address_zip = row
            address = Address(address_id, address_street, address_city, address_zip)
            hotel = Hotel(hotel_id, hotel_name, hotel_stars, address)
            hotels.append(hotel)

        return hotels



