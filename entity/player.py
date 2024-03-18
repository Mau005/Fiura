from configuration.configuration import Configuration
from configuration.constants import Direction
from configuration.constants import LIMIT_VIEW_PLAYER_Y, LIMIT_VIEW_PLAYER_X, TypeObject
from core.animation import Animation
from core.coordinates import Coordinates
from core.core import ManagerDataInternal, TypeFlag
from core.manager_object import ManagerObject
from entity.outfits import Outfits
from kivy.uix.label import Label
from core.collider import Collider
class Player(Outfits):
    def __init__(self, manager: ManagerObject,id_outfits, name_player:str, coordinates: Coordinates, configuration: Configuration, **kwargs):
        self.Name = name_player
        super().__init__(manager, coordinates, id_outfits, configuration, name=self.Name,**kwargs)
        
        self.Health = 100 if kwargs.get("Health") is None else kwargs.get("Health")
        self.HealthMax = 100 if kwargs.get("HealthMax") is None else kwargs.get("HealthMax")
        self.flag = TypeFlag.PLAYER
        self.speed = 3.5
        self.collider.percentage_x_pos = .3
        self.collider.percentage_y_pos = .2
        self.collider.quad_percentage_x = .35
        self.collider.quad_percentage_y = .5

    def draw(self, **kwargs):
        limit_size = kwargs.get("limit_size")
        self.pos = [LIMIT_VIEW_PLAYER_X * limit_size[0], LIMIT_VIEW_PLAYER_Y * limit_size[1]]
        self.animation.draw(**kwargs)   
        super().draw(**kwargs)
        return 

    def movement(self, coord: Coordinates, dt):
        speed = self.speed * dt
        if coord.x > 0:
            self.coord.x += speed
            self.animation.set_direction(Direction.EAST)
        if coord.x < 0:
            self.coord.x -= speed
            self.animation.set_direction(Direction.WEST)
        if coord.y > 0:
            self.coord.y += speed
            self.animation.set_direction(Direction.NORTH)
        if coord.y < 0:
            self.coord.y -= speed
            self.animation.set_direction(Direction.SOUTH)
        return speed, coord, self.animation.direction_flag

    def update(self, **kwargs):
        pass

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print("Soy yo", touch.pos)
