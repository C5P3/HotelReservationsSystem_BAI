from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.Hotel import Hotel

class Room:
    def __init__(self, room_id: int, hotel: Hotel, room_number: int, type_id: int, price_per_night: float):
        self._room_id = room_id
        self._hotel = hotel
        self._room_number = room_number
        self._type_id = type_id
        self._price_per_night = price_per_night


    @property
    def hotel(self) -> Hotel:
        return self._hotel
    
    @hotel.setter
    def hotel(self, hotel: Hotel):
        if hotel is not None and not isinstance(hotel, Hotel):
            raise ValueError("artist must be an instance of Artist")
        # Only do something if the artist is not already the same, prevents recursion!
        if self._hotel is not hotel:
            if self._hotel is not None:
                self._hotel.remove_room(self)
            self._hotel = hotel
            # TODO: Add comment here why we check for None (if we not actually delete the artist)
            if hotel is not None and self not in hotel.rooms:
                hotel.add_album(self)