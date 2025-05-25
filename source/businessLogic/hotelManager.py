from dataAccess.hotelAccess import HotelAccess
from model.Hotel import Hotel


class HotelManager:

    def __init__(self):
        self.__hotel_access = HotelAccess()
    
    def search_hotels_by_city(self, city: str) -> list[Hotel]:
        return self.__hotel_access.get_hotel_by_city(city)
    
    def search_hotels_by_city_and_stars(self, city: str, stars: int) -> list[Hotel]:
        return self.__hotel_access.get_hotel_by_city_and_stars(city, stars)
    
    def search_hotels_by_city_and_max_guests(self, city: str, max_guests: int) -> list[Hotel]:
        return self.__hotel_access.get_hotel_by_city_and_max_guests(city, max_guests)
    
    def search_hotels_by_city_and_dates(self, city: str, check_in_date: str, check_out_date: str) -> list[Hotel]:
        return self.__hotel_access.get_hotel_by_city_and_dates(city, check_in_date, check_out_date)

    



