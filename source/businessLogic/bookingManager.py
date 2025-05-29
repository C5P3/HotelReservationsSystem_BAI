from datetime import date

from dataAccess.bookingAccess import BookingAccess
from model.Booking import Booking

class BookingManager:

    def __init__(self):
        self.__booking_access = BookingAccess()

    def create_booking(self, guest_id: int, room_id: int, check_in_date: date, check_out_date: date, total_amount: float):
        return self.__booking_access(guest_id, room_id, check_in_date, check_out_date, total_amount)
