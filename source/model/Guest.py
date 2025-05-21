class Guest:
    def __init__(self, guest_id: int, first_name: str, last_name: str, email: str, address_id: int):
        self._guest_id = guest_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._address_id = address_id
    