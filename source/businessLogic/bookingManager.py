from datetime import date

from dataAccess.bookingAccess import BookingAccess
from model.Booking import Booking

class BookingManager:

    def __init__(self):
        self.__booking_access = BookingAccess()

    def create_booking(self, guest_id: int, room_id: int, check_in_date: date, check_out_date: date, total_amount: float):
        return self.__booking_access.add_booking(guest_id, room_id, check_in_date, check_out_date, total_amount)
    
    # Evtl. Löschen, da man bei einer Suche alles eingeben bzw. bereits wissen muss
    def search_all_bookings(self, booking_id: int, guest_id: int, room_id: int, check_in_date: date, check_out_date: date, is_cancelled: bool, total_amount: float):
        return self.__booking_access(booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
    
    def get_all_bookings(self):
        return self.__booking_access.get_all_bookings()
    
    def update_booking(self, booking_id, guest_id=None, room_id=None, check_in_date=None, check_out_date=None, is_cancelled=None, total_amount=None):
        return self.__booking_access.update_booking(booking_id, guest_id=guest_id, room_id=room_id, check_in_date=check_in_date, check_out_date=check_out_date, is_cancelled=is_cancelled, total_amount=total_amount)
    
    def search_booking_by_guest(self, guest_id: int) -> list[Booking]:
        return self.__booking_access.get_bookings_by_guest(guest_id)
    
    def cancel_booking(self, booking_id: int) -> bool:
        booking = self.__booking_access.get_booking_by_id(booking_id)
        if not booking:
            print("Buchung nicht gefunden.")
            return False
        if booking.is_cancelled:
            print("Buchung ist bereits storniert.")
            return False
        success = self.__booking_access.update_booking(booking_id, is_cancelled=True)
        return success

    

    

    

