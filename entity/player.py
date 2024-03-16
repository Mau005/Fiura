
from core.coordinates import Coordinates
from core.managerobject import ManagerObject
from core.animation import Animation
from entity.entity import Entity
from configuration.constants import LIMIT_VIEW_PLAYER_Y, LIMIT_VIEW_PLAYER_X, TypeObject


from core.core import TypeFlag



class Player(Entity):

    def __init__(self, manager_obj: ManagerObject, id_outfit, coordinates: Coordinates, **kwargs):
        super().__init__(coordinates, **kwargs)
        self.manager = manager_obj
        self.animation = Animation(id_outfit, manager_obj, self.rectangle, TypeObject.OUTFITS)
        self.Name = kwargs.get("Name")
        self.Health = 100 if kwargs.get("Health") is None else kwargs.get("Health")
        self.HealthMax = 100 if kwargs.get("HealthMax") is None else kwargs.get("HealthMax")
        self.flag = TypeFlag.PLAYER
        self.speed = 1.2
        
        
    def draw(self, **kwargs):
        #Actions Animations
        limit_size = kwargs.get("limit_size")
        self.pos = [LIMIT_VIEW_PLAYER_X* limit_size[0], LIMIT_VIEW_PLAYER_Y* limit_size[1]]
        self.animation.draw(**kwargs)
        return super().draw(**kwargs)
    
    def movemens(self, coord:Coordinates, dt):
        speed =  self.speed * dt
        if coord.x > 0:
            self.coord.x +=  speed
        if coord.x < 0:
            self.coord.x -=  speed
        if coord.y > 0:
            self.coord.y += speed
        if coord.y < 0:
            self.coord.y -= speed
        return [speed, coord]
            
    
    def update(self, *args):
        pass

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print("Widget presionado en posición:", touch.pos)
