from dataAccess.invoiceAccess import InvoiceAccess
from model.Invoice import Invoice

class InvoiceManager: 
    def __init__(self):
        self._invoice_access = InvoiceAccess()

    def get_invoice(self, booking_id: int, total_amount: float):
        self._invoice_access.create_invoice_for_booking(booking_id, total_amount)

