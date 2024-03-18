from configuration.configuration import Configuration
from configuration.constants import TypeObject
from core.animation import Animation
from core.coordinates import Coordinates
from core.core import ManagerDataInternal
from core.manager_object import ManagerObject
from entity.item import Item


class Floor(Item):
    def __init__(self, manager: ManagerObject, coordinates: Coordinates, item_factory: ManagerDataInternal, configuration: Configuration, **kwargs):
        super().__init__(manager, coordinates, item_factory, configuration=configuration, **kwargs)
