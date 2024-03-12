from core.coordinates import Coordinates
from entity.entity import Entity

class Floor(Entity):
    def __init__(self, coordinates: Coordinates, limit_size, source_texture=None, **kwargs):
        super().__init__(coordinates, limit_size, source_texture, **kwargs)
        
