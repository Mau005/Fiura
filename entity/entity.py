from kivy.graphics import Rectangle
from kivy.uix.widget import Widget

from core.coordinates import Coordinates
from core.core import TypeFlag


class Entity(Widget):
    def __init__(self, coordinates: Coordinates, source_texture=None, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = [None, None]
        self.coord = coordinates if coordinates is not None else Coordinates(0, 0, 0)

        self._flag = None
        with self.canvas:
            self.rectangle = Rectangle(size=self.size, pos=self.pos,
                                       source=source_texture if source_texture is not None else "")

    @property
    def flag(self):
        return self._flag

    @flag.setter
    def flag(self, flag):
        self._flag = flag

    def __adjust_canvas(self, **kwargs):
        limit_size = kwargs.get("limit_size")
        #if not (limit_size[0] == self.size[0] and self.size[1] == limit_size[1]):
        if not (self.flag == TypeFlag.PLAYER):
            self.pos = [self.coord.x * limit_size[0], self.coord.y * limit_size[1]]

        self.rectangle.size = limit_size
        self.rectangle.pos = self.pos
        self.size = limit_size

    def draw(self, **kwargs):
        self.__adjust_canvas(**kwargs)
        kwargs.get("canvas").add(self.rectangle)

    def draw_square(self, **kwargs):
        pass
    
    def movemens(self, coord, speed):
        if coord.x > 0:
            self.coord.x -=  speed
        if coord.x < 0:
            self.coord.x +=  speed
        if coord.y > 0:
            self.coord.y -= speed
        if coord.y < 0:
            self.coord.y += speed

    def update(self, **kwargs):
        if not (self.flag == TypeFlag.PLAYER):
            speed, coord = kwargs.get("player_cord")
            self.movemens(coord,speed)
        pass
