from datetime import date
from dataAccess.baseDataAccess import BaseDataAccess

class BookingAccess(BaseDataAccess):
    def get_conflicting_bookings(self, room_id, check_in_date, check_out_date):
        query = """
            SELECT booking_id FROM Booking
            WHERE room_id = ?
            AND is_cancelled = 0
            AND (
                (check_in_date < ? AND check_out_date > ?) OR
                (check_in_date >= ? AND check_in_date < ?) OR
                (check_out_date > ? AND check_out_date <= ?)
            )
        """
        params = (room_id, check_out_date, check_in_date, check_in_date, check_out_date, check_in_date, check_out_date)
        rows = self.execute(query, params, fetch_all=True)
        return len(rows) > 0
    
    def calculate_days_per_stay(self, booking_id:int, check_in_date:date, check_out_date:date):
        query_check_in_date = """ SELECT check_in_date FROM Booking WHERE booking_id = ? """
        params = tuple ([booking_id])
        check_in_date = self.execute(query_check_in_date, params)
        
        query_check_out_date = """ SELECT check_out_date FROM Booking WHERE booking_id = ? """
        params = tuple ([booking_id])
        check_out_date= self.execute(query_check_out_date, params)

        calculate_days = check_out_date - check_in_date
    
        