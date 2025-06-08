from dataAccess.baseDataAccess import BaseDataAccess
from dataAccess.userAccess import UserAccess

class UserManager:
    def __init__(self):
        self.__user_access = UserAccess()
        self.__base_data_access = BaseDataAccess()

    def is_admin(self, username, password):
        return username == "Admin" and password == "FHNW"
    
    
    