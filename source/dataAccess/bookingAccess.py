import os
import sqlite3
from datetime import date

from dataAccess.baseDataAccess import BaseDataAccess
from model.Booking import Booking

class BookingAccess(BaseDataAccess):

    def __init__(self, db_connection_str = None):
        super().__init__(db_connection_str)

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
        
        query_check_out_date = """ 
        SELECT check_out_date 
        FROM Booking 
        WHERE booking_id = ? 
        """
        params = tuple ([booking_id])
        check_out_date= self.execute(query_check_out_date, params)

        calculate_days = check_out_date - check_in_date
    
        
        rows = self.execute(query, params, fetch_all=True)
        return len(rows) > 0
    
    def add_booking(self, guest_id: int, room_id: int, check_in_date: date, check_out_date: date, total_amount: float):
        query = """
        INSERT INTO Booking 
        (guest_id, room_id, check_in_date, check_out_date, total_amount)
        VALUES (?, ?, ?, ?, ?)
        """
        params = (guest_id, room_id, check_in_date, check_out_date, total_amount)
        lastrowid, _ = self.execute(query, params)
        return lastrowid

    def update_booking(self, booking_id: int, guest_id: int = None, room_id: int = None, check_in_date: date = None, check_out_date: date = None, is_cancelled: bool = None, total_amount: float = None):
        
        updates = []
        params = []

        if guest_id is not None:
            updates.append("guest_id = ?")
            params.append(guest_id)
        if room_id is not None:
            updates.append("room_id = ?")
            params.append(room_id)
        if check_in_date is not None:
            updates.append("check_in_date = ?")
            params.append(check_in_date)
        if check_out_date is not None:
            updates.append("check_out_date = ?")
            params.append(check_out_date)
        if is_cancelled is not None:
            updates.append("is_cancelled = ?")
            params.append(1 if is_cancelled else 0) 
        if total_amount is not None:
            updates.append("total_amount = ?")
            params.append(total_amount)

        query = f"UPDATE Booking SET {', '.join(updates)} WHERE booking_id = ?"
        params.append(booking_id) 
        result_tuple = self.execute(query, tuple(params))
        rowcount = result_tuple[1]        
        return True

    def get_all_bookings (self, booking_id: int, guest_id: int, room_id: int, check_in_date: date, check_out_date: date, is_cancelled: bool, total_amount: float):
        query = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount 
        FROM Booking
        """        
        all_bookings = self.fetchall(query)
        return tuple(all_bookings)
    
