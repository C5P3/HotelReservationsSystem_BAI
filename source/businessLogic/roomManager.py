import sqlite3
from datetime import date, datetime, timedelta

from dataAccess.baseDataAccess import BaseDataAccess
from dataAccess.bookingAccess import BookingAccess
from dataAccess.roomAccess import RoomAccess
from dataAccess.hotelAccess import HotelAccess

class RoomManager:

    def __init__(self):
        self.bookingAccess = BookingAccess()
        self.baseDataAccess = BaseDataAccess()
        self.room_access = RoomAccess()
        self.hotel_access = HotelAccess() 

    def find_available_rooms_for_guest(self, check_in_date_str: date, check_out_date_str: date, city: str = None, room_type_description: str = None, num_guests: int = None):
        try:
            check_in_date = datetime.strptime(check_in_date_str, '%Y-%m-%d').date()
            check_out_date = datetime.strptime(check_out_date_str, '%Y-%m-%d').date()
        except ValueError:
            return False

        if check_out_date <= check_in_date:
            return False

        available_rooms = self.room_access.find_available_rooms(
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            city=city,
            room_type_description=room_type_description,
            max_guests_needed=num_guests)
        return available_rooms

    def get_normal_price_per_night(self, room_id: int):
        query = "SELECT price_per_night FROM Room WHERE room_id = ?"
        row = self.room_access.fetchone(query, (room_id,))
        if row:
            return row['price_per_night']
        return None

    def calculate_dynamic_room_price(self, room_id: int, check_in_date_str: str, check_out_date_str: str):
        base_price = self.get_normal_price_per_night(room_id)
        if base_price is None:
            return None 

        check_in_date = datetime.strptime(check_in_date_str, '%Y-%m-%d').date()
        check_out_date = datetime.strptime(check_out_date_str, '%Y-%m-%d').date()
        
        if check_out_date <= check_in_date:
            return None

        high_season_factor = 1.20 
        low_season_factor = 0.80  
        
        total_nights = (check_out_date - check_in_date).days

        daily_prices = []
        for i in range(total_nights):
            day = check_in_date + timedelta(days=i)
            
            current_daily_price = base_price
            
            if day.month in [1, 2, 5, 6, 7, 8, 12]:
                current_daily_price *= high_season_factor
            elif day.month in [3, 4, 9, 10, 11]:
                current_daily_price *= low_season_factor
            
            daily_prices.append(current_daily_price)
        
        if daily_prices:
            return sum(daily_prices) / len(daily_prices)
        else:
            return base_price 

    def calculate_total_price_per_stay(self, room_id: int, check_in_date_str: str, check_out_date_str: str):
        check_in_date = datetime.strptime(check_in_date_str, '%Y-%m-%d').date()
        check_out_date = datetime.strptime(check_out_date_str, '%Y-%m-%d').date()
        
        if check_out_date <= check_in_date:
            return None

        dynamic_price_per_night = self.calculate_dynamic_room_price(room_id, check_in_date_str, check_out_date_str)
        
        if dynamic_price_per_night is None:
            return None
        
        total_nights = (check_out_date - check_in_date).days
        
        return dynamic_price_per_night * total_nights

    def get_all_rooms_details_with_facilities(self):
        rooms_data = self.room_access.get_all_rooms_with_facilities()
        return rooms_data