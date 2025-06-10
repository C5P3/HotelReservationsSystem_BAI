import sqlite3

from dataAccess.baseDataAccess import BaseDataAccess
from model.Facility import Facility

class FacilityAccess(BaseDataAccess):
    def __init__(self, db_connection_str = None):
        super().__init__(db_connection_str)

    def add_facility(self, facility_name):
        query = "INSERT INTO Facilities (facility_name) VALUES (?)"
        self.execute(query, (facility_name,))
        return True

    def update_facility(self, facility_id, facility_name):
        query = "UPDATE Facilities SET facility_name = ? WHERE facility_id = ?"
        self.execute(query, (facility_name, facility_id))
        return True

    def delete_facility(self, facility_id):
        query = "DELETE FROM Facilities WHERE facility_id = ?"
        self.execute(query, (facility_id,))
        return True
