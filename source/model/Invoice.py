from datetime import date

class Invoice:
    def __init__(self, invoice_id: int, booking_id: int, issue_date: date, total_amount: float):
        self._invoice_id = invoice_id
        self._booking_id = booking_id
        self._issue_date = issue_date
        self._total_amount = total_amount

    @property
    def invoice_id(self) -> int:
        return self._invoice_id
    
    @property
    def booking_id(self) -> int:
        return self.booking_id
    
    @property
    def issue_date(self) -> date:
        return self.issue_date
    
    @property
    def total_amount(self) -> float:
        return self.total_amount
    
        