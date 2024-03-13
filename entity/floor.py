from core.coordinates import Coordinates
from entity.entity import Entity


class Floor(Entity):
    def __init__(self, coordinates: Coordinates, source_texture=None, **kwargs):
        super().__init__(coordinates, source_texture, **kwargs)
