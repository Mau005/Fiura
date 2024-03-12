
from configuration.constants import TypeObject, TypeFlag, ErrorType, DataIdentifier
from entity.objects import ObjectIntenal, ItemsInternal
import json

class Core:
    def __init__(self) -> None:
        pass
    
    
    def import_json_default(self, path_file) -> dict:
        with open(path_file, "r") as file:
            return json.load(file)
    
    def __type_check_enums(self,idstr:str) ->int:
        if isinstance(idstr, int):
            return idstr
        if idstr.isnumeric():
            return  int(idstr)
        else:
            raise Exception(ErrorType.ERROR_TYPE.value)
    
    def transform_type_object(self, idStr:str) -> TypeObject:
        """Method usign for transform data.json to typeobject internal

        Args:
            idStr (str): id for datajson

        Raises:
            Exception: not found type data

        Returns:
            TypeObject: convert idflag in to enum
        """
        id_value = self.__type_check_enums(idStr)
        if id_value == TypeObject.FLOOR.value:
            return TypeObject.FLOOR
        elif id_value == TypeObject.EDGES.value:
            return TypeObject.EDGES
        elif id_value == TypeObject.ENTITY.value:
            return TypeObject.ENTITY
        elif id_value == TypeObject.OBJECT_SOLID.value:
            return TypeObject.OBJECT_SOLID
        elif id_value == TypeObject.OBJECT_NOT_SOLID.value:
            return TypeObject.OBJECT_NOT_SOLID
        elif id_value == TypeObject.PICKABLE.value:
            return TypeObject.PICKABLE
        elif id_value == TypeObject.DRINKABLE.value:
            return TypeObject.DRINKABLE
        else:
            raise Exception(ErrorType.ERROR_FLAG.value)
        
        
    def transform_type_flag(self, idStr:str) -> TypeFlag:
        id_value = self.__type_check_enums(idStr)
        if id_value == TypeFlag.PLAYER.value:
            return TypeObject.PLAYER
        elif id_value == TypeFlag.ENEMY.value:
            return TypeObject.ENEMY
        elif id_value == TypeFlag.NPC.value:
            return TypeObject.NPC
        elif id_value == TypeFlag.SOUND.value:
            return TypeObject.SOUND
        else:
            raise Exception(ErrorType.ERROR_FLAG)
        
    def preparing_data_internal(self, file_path, data_ident:DataIdentifier) -> dict:
        new_data = {}
        data = self.import_json_default(file_path)
        for key in data.keys():
            key_proceisng = int(key)
            if data_ident == DataIdentifier.DATA:
                obj = ObjectIntenal(data.get(key))
                obj.TypeFlag = self.transform_type_object(obj.TypeFlag)
                new_data.update({key_proceisng: obj})
            elif data_ident == DataIdentifier.ITEMS:
                new_data.update({key_proceisng: ItemsInternal(data.get(key))})
            else:
                raise Exception(ErrorType.ERROR_TYPE)
        return new_data
        