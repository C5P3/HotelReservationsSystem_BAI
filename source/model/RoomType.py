class RoomType:
    def __init__(self, type_id: int, description: str, max_guests: int):
        self._type_id = type_id
        self._description = description
        self._max_guests = max_guests

    @property
    def type_id(self):
        return self._type_id

    @property
    def description(self):
        return self._description

    @property
    def max_guests(self):
        return self._max_guests

    def __str__(self):
        return f"RoomType(ID: {self.type_id}, Description: {self.description}, Max Guests: {self.max_guests})"

    def to_dict(self):
        return {
            "type_id": self.type_id,
            "description": self.description,
            "max_guests": self.max_guests
        }
        