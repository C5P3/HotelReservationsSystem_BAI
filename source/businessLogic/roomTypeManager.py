from dataAccess.roomTypeAccess import RoomTypeAccess
from dataAccess.baseDataAccess import BaseDataAccess

from model.RoomType import RoomType

class RoomTypeManager:

    def __init__(self):
        self.__roomType_access = RoomTypeAccess()
        self.__baseDataAccess = BaseDataAccess()

    def add_room_type(self, description, max_guests):
        return self.__roomType_access.add_room_type(description, max_guests)

    def update_room_type(self, type_id, description=None, max_guests=None):
        return self.__roomType_access.update_room_type(type_id, description, max_guests)

    def delete_room_type(self, type_id):
        return self.__roomType_access.delete_room_type(type_id)

    def get_room_type_by_id(self, type_id: int):
        return self.__roomType_access.get_all_room_types
    
    def get_room_by_description(self, description: str):
        return self.__roomType_access.get_room_type_by_description

    def get_all_room_types(self):
        return self.__roomType_access.get_all_room_types
