from dataAccess.facilityAccess import FacilityAccess
from dataAccess.baseDataAccess import BaseDataAccess

from model.Facility import Facility

class FacilityManager:

    def __init__(self):
        self.__facility_access = FacilityAccess()
        self.__baseDataAccess = BaseDataAccess()
    
    def add_facility(self, facility_name):
        return self.__facility_access.add_facility(facility_name)

    def update_facility(self, facility_id, facility_name):
        return self.__facility_access.update_facility(facility_id, facility_name)
    
    def delete_facility(self, facility_id):
        return self.__facility_access.delete_facility(facility_id)
    
