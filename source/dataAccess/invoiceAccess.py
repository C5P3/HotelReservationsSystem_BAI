import os
import sqlite3
from datetime import date

from dataAccess.baseDataAccess import BaseDataAccess
from model.Invoice import Invoice
from model.Booking import Booking

class InvoiceAccess(BaseDataAccess):

    def __init__(self, db_connection_str = None):
        super().__init__(db_connection_str)

    def create_invoice_for_booking(self, booking_id: int, total_amount: float):
        today = date.today().isoformat()  # Datumsformat: 'YYYY-MM-DD'
        
        query = """
        INSERT INTO Invoice (booking_id, issue_date, total_amount)
        VALUES (?, ?, ?)      
        """
        params = (booking_id, today, total_amount)
        results = self.execute(query, params)

