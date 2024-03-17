from configuration.constants import TypeObject
from core.animation import Animation
from core.coordinates import Coordinates
from core.managerobject import ManagerObject
from entity.entity import Entity


class Edge(Entity):
    def __init__(self, manager: ManagerObject, id_sprite: int, coordinates: Coordinates, type_object: TypeObject,
                 source_texture=None, **kwargs):
        super().__init__(coordinates, source_texture, **kwargs)

        if type_object.OBJECT_SOLID:
            self.collision = True

        self.manager = manager
        self.animation = Animation(id_sprite, self.manager, self.rectangle, TypeObject.FLOOR)

        # self.status_animations = self.animation.

    def draw(self, **kwargs):
        self.animation.draw(**kwargs)
        return super().draw(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print(f"description: {self.animation.object_internal.name}")
