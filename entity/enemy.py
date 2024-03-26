from configuration.configuration import Configuration
from configuration.constants import TypeFlag
from core.coordinates import Coordinates
from core.manager_object import ManagerObject
from entity.outfits import Outfits


class Enemy(Outfits):
    def __init__(self, manager: ManagerObject,coordinates: Coordinates, id_outfits, configuration: Configuration, name="" , **kwargs):
        super().__init__(manager, coordinates, id_outfits, configuration, **kwargs)
        self.flag = TypeFlag.ENEMY
        self.collider.percentage_x_pos = .3
        self.collider.percentage_y_pos = .2
        self.collider.quad_percentage_x = .35
        self.collider.quad_percentage_y = .5
        self.label_name.text = name
        self.animation.status_animation = False
