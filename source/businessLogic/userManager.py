from dataAccess.baseDataAccess import BaseDataAccess

class UserManager:
    def __init__(self):
        self.__base_data_access = BaseDataAccess()

    def is_admin(self, username, password):
        return username == "Admin" and password == "FHNW"
    
    
    