from dataAccess.baseDataAccess import BaseDataAccess
from model.Address import Address


class AddressAccess(BaseDataAccess):
    def get_address_by_id(self, address_id):
        query = "SELECT address_id, street, city, zip_code FROM Address WHERE address_id = ?"
        row = self.execute(query, (address_id,), fetch_one=True)
        if row:
            return Address(*row)
        return None

    def add_address(self, street:str, city:str, zip_code:int):
        query_highest_id = """ SELECT MAX(address_id) FROM Address """
        result_highest_id = self.fetchone(query_highest_id)
        if result_highest_id is None:
            result_highest_id = 0
        
        query_add_address = "INSERT INTO Address (?, ?, ?, ?)"
        self.execute(query_add_address, (result_highest_id + 1, street, city, zip_code))
        return True
 
    def update_address(self, address_id:int, street:str = None, city:str = None, zip_code:int = None):
        query = " UPDATE address SET "
        fields = []
        params = []

        if street is not None:
            fields.append("street = ?")
            params.append(street) 
        if city is not None:
            fields.append("city = ?")
            params.append(city) 
        if zip_code is not None:
            fields.append("zip_code = ?")
            params.append(zip_code) 
        
        result = self.execute(query, tuple(params))

        if result == 0:
            return False
        else:
            return True

    def delete_address(self, address_id:int):
        query = """ DELETE FROM Address WHERE address_id"""
        row_deleted = self.execute(query, (address_id,))
        if row_deleted < 1:
             return False
        else:
            return True
