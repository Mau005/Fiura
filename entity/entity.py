from core.coordinates import Coordinates
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

class Entity(Widget):
    def __init__(self, coordinates:Coordinates, limit_size, source_texture=None, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = [None, None]
        self._coord = coordinates if coordinates is not None else Coordinates(0,0,0)
        self.pos = [coordinates.x * limit_size[0], coordinates.y * limit_size[1]]
        
        self._flag = None
        print(f"Posicion = ", self.pos, " Tamanio: ",self.size)
        with self.canvas:
            self._rectangle = Rectangle(size = self.size, pos = self.pos, source= source_texture if source_texture is not None else "")

    @property
    def flag(self):
        return self._flag
    
    @flag.setter
    def flag(self, flag):
        self._flag = flag
        
    @property
    def position(self):
        return self._coord
    
    @position.setter
    def position(self, coord: Coordinates):
        self._coord = Coordinates
        
    def __adjust_canvas(self, **kwargs):
        limit_size = kwargs.get("limit_size")
        if not(limit_size[0] == self.size[0] and self.size[1] == limit_size[1]):
            self.pos = [self._coord.x * limit_size[0], self._coord.y * limit_size[1]]
            
        self._rectangle.size = limit_size
        self._rectangle.pos = self.pos
        self.size = limit_size
        
        
    def draw(self, **kwargs):
        self.__adjust_canvas(**kwargs)
        kwargs.get("canvas").add(self._rectangle)
        
    
    def draw_square(self, **kwargs):
        pass
    
    
    def update(self, *args):
        pass
        