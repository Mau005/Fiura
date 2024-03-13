import json
from typing import Optional

from configuration.constants import TypeObject, TypeFlag, ErrorType, DataIdentifier, Direction, Gender


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
    elif id_value == TypeObject.PICKABLE.value:
        return TypeObject.PICKABLE
    elif id_value == TypeObject.DRINKABLE.value:
        return TypeObject.DRINKABLE
    elif id_value == TypeObject.OUTFITS.value:
        return TypeObject.OUTFITS
    else:
        raise Exception(ErrorType.ERROR_FLAG.value)


def transform_direction(payload: dict) -> dict:
    print(payload)
    content = payload.get("DirectionSprite")
    if content is None:
        return {}
    return {
        Direction.NORTH: content.get("1", []),
        Direction.SOUTH: content.get("2", []),
        Direction.WEST: content.get("3", []),
        Direction.EAST: content.get("4", []),
    }


class DataInternal:
    def __init__(self, payload: dict) -> None:
        self.TypeFlag: Optional[TypeObject] = transform_type_object(payload.get("TypeFlag"))
        self.NameSprite: Optional[str] = payload.get("NameSprite")
        self.Sprites: Optional[list] = payload.get("Sprites")
        self.Animation: Optional[bool] = payload.get("Animation")
        self.AnimatedSequence = tuple(payload.get("AnimatedSequence", []))
        self.DirectionSprite: Optional[dict] = transform_direction(payload)

    def __str__(self) -> str:
        return '''
        self.TypeFlag = {}
        self.NameSprite = {}
        self.Sprites = {}
        self.Animation = {}
        self.AnimatedSequence = {}
        self.DirectionSprite = {}

    '''.format(self.TypeFlag, self.NameSprite, self.Sprites, self.Animation, self.AnimatedSequence,
               self.DirectionSprite)


class ManagerDataInternal:
    def __init__(self, payload):
        self.IDDataFactory = payload.get("IDDataFactory")
        self.DataFactory: Optional[DataInternal] = None

    def add_data_factory(self, data_factory: DataInternal):
        self.DataFactory = data_factory


class OutfitsInternal(ManagerDataInternal):
    def __init__(self, payload):
        super().__init__(payload)
        self.FileSprite = payload.get("FileSprite")
        self.Gender = transform_gender_flag(payload.get("Gender"))
        self.Name = payload.get("Name")


class ItemInternal(ManagerDataInternal):
    def __init__(self, payload: dict) -> None:
        super().__init__(payload)
        self.Name = payload.get("Name")
        self.Description = payload.get("Description")

    def __str__(self):
        return '''
        seslf.self.IDDataFactory = {}
        self.Name = {}
        self.Description = {}
        self.Object = {}
        '''.format(self.IDDataFactory, self.Name, self.Description, self.DataFactory)


class Core:
    def __init__(self) -> None:
        pass

    def import_json_default(self, path_file) -> dict:
        with open(path_file, "r") as file:
            return json.load(file)

    def __type_check_enums(self, idstr: str) -> int:
        if isinstance(idstr, int):
            return idstr
        if idstr.isnumeric():
            return int(idstr)
        else:
            raise Exception(ErrorType.ERROR_TYPE.value)

    def transform_type_flag(self, id_str: str) -> TypeFlag:
        id_value = self.__type_check_enums(id_str)
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

    def preparing_data_internal(self, file_path, data_indent: DataIdentifier) -> dict:
        new_data = {}
        data = self.import_json_default(file_path)
        for key in data.keys():
            key_proceeding = int(key)
            if data_indent == DataIdentifier.DATA:
                new_data.update({key_proceeding: DataInternal(data.get(key))})
            elif data_indent == DataIdentifier.ITEMS:
                new_data.update({key_proceeding: ItemInternal(data.get(key))})
            elif data_indent == DataIdentifier.OUTFITS:
                new_data.update({key_proceeding: OutfitsInternal(data.get(key))})
            else:
                raise Exception(ErrorType.ERROR_TYPE)
        return new_data
