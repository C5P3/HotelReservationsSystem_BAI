from datetime import date
class Invoice:
    def __init__(self, invoice_id: int, booking_id: int, issue_date: date, total_amount: float):
        self._invoice_id = invoice_id
        self._booking_id = booking_id
        self._issue_date = issue_date
        self.total_amount = total_amount
        