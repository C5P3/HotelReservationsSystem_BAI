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
        