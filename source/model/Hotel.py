class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, address_id: int):
        self.id_hotel_id = hotel_id
        self._name = name
        self._stars = stars
        self._address_id = address_id
    