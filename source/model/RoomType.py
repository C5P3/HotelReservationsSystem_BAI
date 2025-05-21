class RoomType:
    def __init__(self, type_id: int, description: str, max_guests: int):
        self._type_id = type_id
        self._description = description
        self._max_guests = max_guests
        