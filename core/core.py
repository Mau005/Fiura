import json
from typing import Optional

from configuration.constants import TypeObject, TypeFlag, ErrorType, DataIdentifier, Direction, Gender
import csv

def read_csv(path_file:str) ->dict:
    data = []
    with open(path_file, 'r', newline='') as file_csv:
        read_csv_iterator = csv.reader(file_csv)
        header = next(read_csv_iterator, None)
        for fila in read_csv_iterator:
            data.append(fila)
    return {"header": header, "data":data}

def transform_direction_flag(id_str) -> Direction:
    ids = int(id_str)
    if ids == Direction.NORTH.value:
        return Direction.NORTH
    elif ids == Direction.EAST.value:
        return Direction.EAST
    elif ids == Direction.WEST.value:
        return Direction.WEST
    elif ids == Direction.SOUTH.value:
        return Direction.SOUTH
    else:
        raise Exception(ErrorType.ERROR_FLAG)


def transform_gender_flag(id_str):
    ids = int(id_str)
    if ids == Gender.MALE.value:
        return Gender.MALE
    elif ids == Gender.FEMALE.value:
        return Gender.FEMALE
    else:
        raise Exception(ErrorType.ERROR_FLAG.value)


def transform_type_object(id_str: str) -> TypeObject:
    id_value = int(id_str)
    if id_value == TypeObject.FLOOR.value:
        return TypeObject.FLOOR
    elif id_value == TypeObject.EDGES.value:
        return TypeObject.EDGES
    elif id_value == TypeObject.OBJECT_SOLID.value:
        return TypeObject.OBJECT_SOLID
    elif id_value == TypeObject.OBJECT_NOT_SOLID.value:
        return TypeObject.OBJECT_NOT_SOLID
    elif id_value == TypeObject.PACKABLE.value:
        return TypeObject.PACKABLE
    elif id_value == TypeObject.DRINKABLE.value:
        return TypeObject.DRINKABLE
    elif id_value == TypeObject.OUTFITS.value:
        return TypeObject.OUTFITS
    else:
        raise Exception(ErrorType.ERROR_FLAG.value)


def transform_direction(payload: dict) -> dict:
    content = payload.get("DirectionSprite")
    if content is None:
        return {}
    return {
        Direction.NORTH: content.get("1", []),
        Direction.SOUTH: content.get("2", []),
        Direction.WEST: content.get("3", []),
        Direction.EAST: content.get("4", []),
    }


class DataFactory:
    def __init__(self, payload: dict) -> None:
        self.type_object: Optional[TypeObject] = transform_type_object(payload.get("TypeObject"))
        self.name_sprite: Optional[str] = payload.get("NameSprite")
        self.collision = True if payload.get("Collision") is not None and payload.get("Collision") else False
        self.status_animation: Optional[bool] = payload.get("Status_Animation")
        self.direction_sprite: Optional[dict] = transform_direction(payload)

    def __str__(self):
        return str(self.__dict__)


class ManagerDataInternal:
    def __init__(self, payload, key:int):
        self.name = payload.get("Name")
        self.id = key
        self.description = payload.get("Description")
        self.id_data_factory = payload.get("IDDataFactory")
        self.data_factory: Optional[DataFactory] = None

    def add_data_factory(self, data_factory: DataFactory):
        self.data_factory = data_factory

    def __str__(self) -> str:
        return str(self.__dict__)


class OutfitsDataInternal(ManagerDataInternal):
    def __init__(self, payload, key):
        super().__init__(payload,key)
        self.gender = transform_gender_flag(payload.get("Gender"))


def import_json_default(path_file) -> dict:
    with open(path_file, "r") as file:
        return json.load(file)


def __type_check_enums(id_str: str) -> int:
    if isinstance(id_str, int):
        return id_str
    if id_str.isnumeric():
        return int(id_str)
    else:
        raise Exception(ErrorType.ERROR_TYPE.value)


def transform_type_flag(id_str: str) -> TypeFlag:
    id_value = __type_check_enums(id_str)
    if id_value == TypeFlag.PLAYER.value:
        return TypeFlag.PLAYER
    elif id_value == TypeFlag.ENEMY.value:
        return TypeFlag.ENEMY
    elif id_value == TypeFlag.NPC.value:
        return TypeFlag.NPC
    elif id_value == TypeFlag.SOUND.value:
        return TypeFlag.SOUND
    else:
        raise Exception(f"ID: {id_value}: {ErrorType.ERROR_FLAG.value}")


def preparing_data_internal(file_path, data_indent: DataIdentifier) -> dict:
    new_data = {}
    data = import_json_default(file_path)
    for key in data.keys():
        key_proceeding = int(key)
        if data_indent == DataIdentifier.DATA:
            new_data.update({key_proceeding: DataFactory(data.get(key))})
        elif data_indent == DataIdentifier.ITEMS:
            new_data.update({key_proceeding: ManagerDataInternal(data.get(key), key)})
        elif data_indent == DataIdentifier.OUTFITS:
            new_data.update({key_proceeding: OutfitsDataInternal(data.get(key), key)})
        else:
            raise Exception(ErrorType.ERROR_FLAG.value)
    return new_data


class Core:
    def __init__(self) -> None:
        pass
