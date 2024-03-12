from enum import Enum, auto

LANGUAGE_PATH_ESP = "data/language/esp.txt"
LANGUAGE_PATH_EN = "data/language/en.txt"


LIMIT_VIEW_X = 16
LIMIT_VIEW_Y  = 10
SQUARE = [32,32]

class DataIdentifier(Enum):
    DATA =auto()
    ITEMS= auto()

class ErrorType(Enum):
    ERROR_FLAG = "ERROR DE FLAG, LA FLAG BUSCADA NO ES ENCONTRADA"
    ERROR_TYPE = "ERROR DE TIPOS DE DATOS, NO COMPATIBLES"


class TypeFlag(Enum):
    PLAYER = "player"
    ENEMY = "enemy"
    NPC = "npc"
    SOUND = "sound"
    

class TypeObject(Enum):
    FLOOR = auto()
    EDGES = auto() 
    ENTITY = auto()
    OBJECT_SOLID =auto()
    OBJECT_NOT_SOLID = auto()
    PICKABLE = auto()
    DRINKABLE = auto()
    

