from dataAccess.baseDataAccess import BaseDataAccess
from model.Address import Address


class AddressAccess(BaseDataAccess):
     def get_address_by_id(self, address_id):
        query = "SELECT address_id, street, city, zip_code FROM Address WHERE address_id = ?"
        row = self._execute_query(query, (address_id,), fetch_one=True)
        if row:
            return Address(*row)
        return None

"""
muss noch überarbeitet werden

    def add_address(self, street, city, zip_code):
        query = "INSERT INTO Address (street, city, zip_code) VALUES (?, ?, ?)"
        return None
 
"""