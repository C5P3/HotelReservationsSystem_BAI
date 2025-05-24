from dataAccess.hotelAccess import HotelAccess
from model.Hotel import Hotel


class HotelManager:
    def __init__(self):
        self.__hotel_access = HotelAccess()
    
    def search_hotels(self, city: str) -> list[Hotel]:
        return self.__hotel_access.get_hotel_by_city(city)


