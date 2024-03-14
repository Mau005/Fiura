from kivy.graphics import Rectangle
from kivy.uix.widget import Widget

from core.coordinates import Coordinates


class Entity(Widget):
    def __init__(self, coordinates: Coordinates, source_texture=None, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = [None, None]
        self._coord = coordinates if coordinates is not None else Coordinates(0, 0, 0)

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

    @property
    def position(self):
        return self._coord

    @position.setter
    def position(self, coord: Coordinates):
        self._coord = Coordinates

    def __adjust_canvas(self, **kwargs):
        limit_size = kwargs.get("limit_size")
        if not (limit_size[0] == self.size[0] and self.size[1] == limit_size[1]):
            self.pos = [self._coord.x * limit_size[0], self._coord.y * limit_size[1]]

        self.rectangle.size = limit_size
        self.rectangle.pos = self.pos
        self.size = limit_size

    def draw(self, **kwargs):
        self.__adjust_canvas(**kwargs)
        kwargs.get("canvas").add(self.rectangle)

    def draw_square(self, **kwargs):
        pass

    def update(self, *args):
        pass
