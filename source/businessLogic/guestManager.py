from dataAccess.guestAccess import GuestAccess

from model.Guest import Guest

class GuestManager:

    def __init__(self):
        self.__guest_access = GuestAccess()

    def search_all_guests(self, guest_id: int = None, first_name: str = None, last_name: str = None, email: str = None, address_id: int = None) -> list[Guest]:
        guests = self.__guest_access.get_all_guests()

        if guest_id is not None:
            guests = [g for g in guests if g.guest_id == guest_id]
        if first_name is not None:
            guests = [g for g in guests if g.first_name.lower() == first_name.lower()]
        if last_name is not None:
            guests = [g for g in guests if g.last_name.lower() == last_name.lower()]
        if email is not None:
            guests = [g for g in guests if g.email.lower() == email.lower()]
        if address_id is not None:
            guests = [g for g in guests if g.address_id == address_id]

        return guests
    


    