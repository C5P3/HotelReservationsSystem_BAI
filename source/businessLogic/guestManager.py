from dataAccess.guestAccess import GuestAccess

from model.Guest import Guest

class GuestManager:

    def __init__(self):
        self.__guest_access = GuestAccess()

    def search_all_guests(self, guest_id: int, first_name: str, last_name: str, email: str, address_id: int):
        return self.__guest_access.get_all_guests()
    
    

    