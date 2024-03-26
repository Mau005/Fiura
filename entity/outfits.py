from entity.entity import Entity
from configuration.configuration import Configuration
from core.coordinates import Coordinates
from entity.entity import Entity
from core.core import ManagerDataInternal
from core.manager_object import ManagerObject
from core.animation import Animation

class Outfits(Entity):
    def __init__(self, manager:ManagerObject, coordinates: Coordinates,id_outfits, configuration: Configuration, **kwargs):
        self.manager = manager
        self.outfits_factory = self.manager.get_outfits_attribute(id_outfits)
        super().__init__(coordinates, configuration=configuration, data_factory=self.outfits_factory.data_factory, **kwargs)
        self.animation = Animation(self.outfits_factory.data_factory, self.manager,self.rectangle)
        self.flag = self.outfits_factory.data_factory.type_object
        self.id_item = self.outfits_factory.id

    def draw(self, **kwargs):
        self.animation.draw(**kwargs)
        return super().draw(**kwargs)
