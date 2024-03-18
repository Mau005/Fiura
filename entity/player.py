from configuration.constants import Direction
from configuration.constants import LIMIT_VIEW_PLAYER_Y, LIMIT_VIEW_PLAYER_X, TypeObject
from core.animation import Animation
from core.coordinates import Coordinates
from core.core import TypeFlag
from core.managerobject import ManagerObject
from entity.entity import Entity
from kivy.uix.label import Label
from core.collider import Collider
class Player(Entity):

    def __init__(self, manager_obj: ManagerObject, id_outfit:int,name_player:str, coordinates: Coordinates, **kwargs):
        super().__init__(coordinates,name=name_player, **kwargs)
        self.manager = manager_obj
        self.animation = Animation(id_outfit, manager_obj, self.rectangle, TypeObject.OUTFITS)
        self.Name = name_player
        self.Health = 100 if kwargs.get("Health") is None else kwargs.get("Health")
        self.HealthMax = 100 if kwargs.get("HealthMax") is None else kwargs.get("HealthMax")
        self.flag = TypeFlag.PLAYER
        self.speed = 3.5
        self.collider =  Collider(.3,.2, .35, .5)
        self.add_widget(self.collider)

    def draw(self, **kwargs):
        limit_size = kwargs.get("limit_size")
        self.pos = [LIMIT_VIEW_PLAYER_X * limit_size[0], LIMIT_VIEW_PLAYER_Y * limit_size[1]]
        self.collider.draw(self.pos, self.size, **kwargs)
        self.animation.draw(**kwargs)   
        super().draw(**kwargs)
        kwargs.get("canvas").add(self.collider.canvas)
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
