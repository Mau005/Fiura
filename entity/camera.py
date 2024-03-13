from core.coordinates import Coordinates
from entity.entity import Entity


class Camera(Entity):
    def __init__(self, coordinates: Coordinates, limit_size, source_texture=None, **kwargs):
        super().__init__(coordinates, limit_size, source_texture, **kwargs)

        self.size_hint = [None, None]

    def draw(self, **kwargs):
        pass

    def draw_square(self, **kwargs):
        pass

    def update(self, *args):
        super().update(*args)
        self.rectangle.pos = self.pos
