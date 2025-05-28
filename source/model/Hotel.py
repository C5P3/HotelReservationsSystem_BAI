from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.Address import Address
    from model.Room import Room

class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, address: Address = None):
        self._hotel_id = hotel_id
        self._name = name
        self._stars = stars
        self._address = address
        self._rooms = []

    @property
    def hotel_id(self) -> int:
        return self._hotel_id
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name:str):
        if not name and isinstance(name, str):
            raise ValueError("Name is required and must be a str")
        self._name = name

    @property
    def rooms(self) -> tuple[Room]:
        return tuple(self._rooms)

    def add_room(self, room: Room):
        # TODO: check if room is not None and room is of instance Room
        if room not in self._rooms:
            self._rooms.append(room)
            room.hotel = self

    def remove_room(self, room: Room):
        if not room:
            raise ValueError("room is required")
        if not isinstance(room, Room):
            raise ValueError("room must be an instance of Room")
        if room in self._rooms:
            self._rooms.remove(room)
            room.hotel = None

    
