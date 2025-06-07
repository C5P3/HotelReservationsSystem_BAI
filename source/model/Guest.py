from __future__ import annotations
from typing import TYPE_CHECKING

class Guest:

    def __init__(self, guest_id: int, first_name: str, last_name: str, email: str, address_id: int):
        self._guest_id = guest_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._address_id = address_id

    @property
    def guest_id(self) -> int:
        return self._guest_id
    
    @property
    def first_name(self) -> str:
        return self._first_name
    
    @property
    def last_name(self) -> str:
        return self._last_name
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def address_id(self) -> int:
        return self._address_id
    

    

    