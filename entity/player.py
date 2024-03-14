
from core.coordinates import Coordinates
from core.managerobject import ManagerObject
from core.animation import Animation
from entity.entity import Entity





class Player(Entity):

    def __init__(self, manager_obj: ManagerObject, id_outfit, coordinates: Coordinates, **kwargs):
        super().__init__(coordinates, **kwargs)
        self.manager = manager_obj
        self.animation = Animation(id_outfit, manager_obj, self.rectangle)
        self.Name = kwargs.get("Name")
        self.Health = 100 if kwargs.get("Health") is None else kwargs.get("Health")
        self.HealthMax = 100 if kwargs.get("HealthMax") is None else kwargs.get("HealthMax")
        
        
    def draw(self, **kwargs):
        #Actions Animations
        self.animation.draw(**kwargs)
        return super().draw(**kwargs)
    
    def update(self, *args):
        pass

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print("Widget presionado en posición:", touch.pos)
