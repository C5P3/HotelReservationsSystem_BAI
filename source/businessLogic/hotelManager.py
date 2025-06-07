from dataAccess.hotelAccess import HotelAccess
from dataAccess.roomAccess import RoomAccess

from model.Hotel import Hotel
from model.Room import Room

class HotelManager:

    def __init__(self):
        self.__hotel_access = HotelAccess()
        self.__room_access = RoomAccess()
        
    def search_all_hotels(self) -> list[Hotel]:
        return self.__hotel_access.get_all_hotels()

    def search_hotels_by_city(self, city: str) -> list[Hotel]:
        return self.__hotel_access.get_hotel_by_city(city,)
    
    def search_hotels_by_city_and_stars(self, city: str, stars: int) -> list[Hotel]:
        return self.__hotel_access.get_hotel_by_city_and_stars(city, stars)
    
    def search_hotels_by_city_and_max_guests(self, city: str, max_guests: int) -> list[Hotel]:
        return self.__hotel_access.get_hotel_by_city_and_max_guests(city, max_guests)
    
    def search_hotels_by_combinations(self, city: str, stars: int, max_guests: int, check_in_date: str, check_out_date: str) -> list[Hotel]:
        return self.__hotel_access.get_hotel_by_combinations(city, stars, max_guests, check_in_date, check_out_date)

    def search_hotel_information(self) -> list[Hotel]:
        return self.__hotel_access.get_hotel_information()
    
    def add_hotel(self, name: str, stars: int, address_id: int):
        return self.__hotel_access.add_hotel(name, stars, address_id)
    
    def update_hotel(self, hotel_id: int, name: str = None, stars: int = None, address_id: int = None):
        return self.__hotel_access.update_hotel(hotel_id, name, stars, address_id)
    
    def delete_hotel(self, hotel_id: int):
        return self.__hotel_access.delete_hotel(hotel_id)
    
    
    



