from dataAccess.addressAccess import AddressAccess
from model.Address import Address

class AddressManager:
       
    def __init__(self):
        self.__address_access = AddressAccess()
    
    def add_address(self, street:str, city:str, zip_code:int):
        return self.__address_access.add_address(street, city, zip_code)

    def update_address(self, address_id:int, street:str = None, city:str = None, zip_code:int = None):
        return self.__address_access.update_address (address_id, street, city, zip_code)

    def delete_address(self, address_id: int):
        return self.__address_access.delete_address(address_id)