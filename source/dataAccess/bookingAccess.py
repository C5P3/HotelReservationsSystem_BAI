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
        rows = self._execute_query(query, params, fetch_all=True)
        return len(rows) > 0