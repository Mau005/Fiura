from configuration.constants import Direction
from core.coordinates import Coordinates
from core.managerobject import ManagerObject
from entity.entity import Entity


class Outfits:
    def __init__(self):
        pass


class Player(Entity):

    def __init__(self, manager_obj: ManagerObject, id_outfit, coordinates: Coordinates, **kwargs):
        self.manager = manager_obj
        self.outfits = self.manager.get_outfits_attribute(id_outfit)
        self.direction_now = self.outfits.DataFactory.DirectionSprite[Direction.SOUTH][0]
        path = self.manager.get_sprite_outfits_id(self.outfits.DataFactory.NameSprite,
                                                  self.direction_now)
        print(path)
        super().__init__(coordinates,
                         source_texture=path, **kwargs)
