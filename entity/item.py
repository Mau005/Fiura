

from configuration.configuration import Configuration
from core.coordinates import Coordinates
from entity.entity import Entity
from core.core import ManagerDataInternal
from core.manager_object import ManagerObject
from core.animation import Animation

class Item(Entity):
    def __init__(self, manager:ManagerObject, coordinates: Coordinates,item_factory:ManagerDataInternal, configuration: Configuration, **kwargs):
        self.manager = manager
        self.item_factory = item_factory
        super().__init__(coordinates, self.item_factory.name, configuration=configuration, data_factory=self.item_factory.data_factory, **kwargs)
        
        
        self.flag = self.item_factory.data_factory.type_object
        self.id_item = self.item_factory.id
        self.animation = Animation(self.item_factory.data_factory,self.manager,self.rectangle)

    def draw(self, **kwargs):
        self.animation.draw(**kwargs)
        return super().draw(**kwargs)
