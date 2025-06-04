from dataAccess.roomTypeAccess import RoomTypeAccess
from dataAccess.baseDataAccess import BaseDataAccess


from model.RoomType import RoomType

class RoomTypeManager:

    def __init__(self):
        self.__roomType_access = RoomTypeAccess()

    def get_room_type_by_id(self, type_id: int):
        return self.__roomType_access.get_all_room_types
    
    def get_room_by_description(self, description: str):
        return self.__roomType_access.get_room_type_by_description
    
    def get_all_room_types(self):
        return self.__roomType_access.get_all_room_types
