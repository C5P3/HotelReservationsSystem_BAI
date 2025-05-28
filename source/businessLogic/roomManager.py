import sqlite3
from datetime import date

from dataAccess.baseDataAccess import BaseDataAccess
from dataAccess.bookingAccess import BookingAccess

class RoomManager:

    def __init__(self):
        self.__bookingAccess = BookingAccess()
        self.__baseDataAccess = BaseDataAccess()

    def variable_price_factor_calculation(self, booking_id, check_in_date:date):
        query = """ SELECT check_in_date FROM Booking WHERE booking_id = ? """
    check_in_date =
    
    if check_in_date >= 11:
        return 1.5
    elif check_in_date >= 7:
        return 1
    elif check_in_date >= 4:   
        return 1.7
    elif check_in_date >= 1:
        return 1.5
    else:
        return 1
    

    def calculate_price_per_night(self, booking_id:int, room_id:int, price_per_night:float):
        query_get_price_per_night = """ 
        SELECT B.room_id,
        R.price_per_night
        FROM Booking AS B
        JOIN Room AS R ON B.room_id = R.room_id;
        """


    def calculate_total_price_per_stay(self, booking_id):