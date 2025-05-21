from datetime import date
class Booking:
    def __init__(self, booking_id: int, guest_id: int, room_id: int, check_in_date: date, check_out_date: date, is_cancelled: bool, total_amount: float):
        self._booking_id = booking_id
        self._guest_id = guest_id
        self._room_id = room_id
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._is_cancelled = is_cancelled
        self._total_amount = total_amount

    @property
    def booking_id(self):
        return self._booking_id
    
    @property
    def guest_id(self):
        return self._guest_id
    
    @property
    def room_id(self):
        return self._room_id
    
    @property
    def check_in_date(self):
        return self._check_in_date
    
    @property
    def check_out_date(self):
        return self._check_out_date
    
    @property
    def is_cancelled(self):
        return self._is_cancelled
    
    @property
    def total_amount(self):
        return self._total_amount