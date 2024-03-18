from enum import Enum, auto

from core.coordinates import Coordinates

LANGUAGE_PATH_ESP = "data/language/esp.txt"
LANGUAGE_PATH_EN = "data/language/en.txt"

LIMIT_VIEW_X = 11
LIMIT_VIEW_Y = 8
LIMIT_VIEW_PLAYER_X = 5
LIMIT_VIEW_PLAYER_Y = 4
SQUARE = [32, 32]


class DataIdentifier(Enum):
    DATA = auto()
    ITEMS = auto()
    OUTFITS = auto()


class ErrorType(Enum):
    ERROR_FLAG = "ERROR DE FLAG, LA FLAG BUSCADA NO ES ENCONTRADA"
    ERROR_TYPE = "ERROR DE TIPOS DE DATOS, NO COMPATIBLES"


class TypeFlag(Enum):
    PLAYER = auto()
    ENEMY = auto()
    NPC = auto()
    SOUND = auto()
    NULL = auto()


class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    WEST = auto()
    EAST = auto()
    NULL = auto()


class KeyboardKey(Enum):
    W = 119
    A = 97
    S = 115
    D = 100


class TypeObject(Enum):
    FLOOR = auto()
    EDGES = auto()
    OBJECT_SOLID = auto()
    OBJECT_NOT_SOLID = auto()
    PACKABLE = auto()
    DRINKABLE = auto()
    OUTFITS = auto()
    FLOOR_ANIMATION = auto()
    NULL = auto()


class DirectionPlayer(Enum):
    NORTH = Coordinates(0, 1, 0)
    WEST = Coordinates(-1, 0, 0)
    EAST = Coordinates(1, 0, 0)
    SOUTH = Coordinates(0, -1, 0)


class Gender(Enum):
    MALE = auto()
    FEMALE = auto()
