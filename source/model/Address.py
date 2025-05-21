class Address:
    def __init__(self, id: int, street: str, city: str, zip: str):
        self._id = id
        self._street = street
        self._city = city
        self._zip = zip

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def street(self) -> str:
        return self._street

    @street.setter
    def street(self, street: str) -> None:
        self._street = street

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, city: str) -> None:
        self._city = city

    @property
    def zip(self) -> str:
        return self._zip

    @zip.setter
    def zip(self, zip_code: str) -> None:
        self._zip = zip_code

    def __str__(self) -> str:
        return "Address(id={0},street={1},zip={2},city={3})".format(
            self._id, self._street, self._zip, self._city
        )

    def to_dict(self):
        return {
            "id": self._id,
            "street": self._street,
            "zip": self._zip,
            "city": self._city,
        }
 


        