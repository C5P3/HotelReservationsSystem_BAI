import os
import sqlite3
from datetime import date

from dataAccess.baseDataAccess import BaseDataAccess
from model.Invoice import Invoice
from model.Booking import Booking

class InvoiceAccess(BaseDataAccess):

    def __init__(self, db_connection_str = None):
        super().__init__(db_connection_str)

    def create_invoice_for_booking(self, booking_id: str,  )