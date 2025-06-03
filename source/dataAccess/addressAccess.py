import sqlite3

from dataAccess.baseDataAccess import BaseDataAccess
from model.Address import Address


class AddressAccess(BaseDataAccess):
    def __init__(self, db_connection_str: str):
        super().__init__(db_connection_str)

    def get_address_by_id(self, address_id):
        query = "SELECT address_id, street, city, zip_code FROM Address WHERE address_id = ?"
        row = self.execute(query, (address_id,), fetch_one=True)
        row = self.fetchone(query, (address_id,))
        if row:
            return Address(row['address_id'], row['street'], row['city'], row['zip_code'])
        return None
    
    def add_address(self, street: str, city: str, zip_code: int = None):
        query = "INSERT INTO Address (street, city, zip_code) VALUES (?, ?, ?)"  
        lastrowid = self.execute(query, (street, city, zip_code))
        return lastrowid

    def update_address(self, address_id: int, street: str = None, city: str = None, zip_code: int = None):
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
        if not fields:
            return False

        query = f"UPDATE Address SET {', '.join(fields)} WHERE address_id = ?"
        params.append(address_id)
        self.execute(query, tuple(params))
        return True

    def delete_address(self, address_id: int):
        query = "DELETE FROM Address WHERE address_id = ?"
        self.execute(query, (address_id,))
        return True 


