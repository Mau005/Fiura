import random
from typing import Optional

from kivy.graphics import Rectangle
from kivy.uix.widget import Widget

from configuration.constants import LIMIT_VIEW_Y, LIMIT_VIEW_X
from configuration.constants import TypeObject
from core.coordinates import Coordinates
from core.core import Core, ItemInternal
from core.managerobject import ManagerObject
from entity.floor import Floor
from maps.map import Map


class Render(Widget):
    def __init__(self, window, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = [None, None]
        self.size = window
        self.core = Core()
        self.manager_object = ManagerObject(self.core)

        self.map = Map(100, 100)
        for index in range(0, 1000):
            self.map.set_position_map(Coordinates(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)),
                                      random.randint(0, 3), )

        self.render_layers = {
            1: [],  # Floor
            2: [],  # edge
            3: [],  # object
            4: [],  # entity
            5: []  # object_upper
        }
        with self.canvas.before:
            # self.fbo = Fbo(size=self.size)
            self.rectangle = Rectangle(pos=self.pos, size=self.size)

        self.init_map()

    def init_map(self):
        for x in range(self.map.get_len_map_x()):
            for y in range(self.map.get_len_map_y(x)):
                items: Optional[ItemInternal] = self.manager_object.get_items_attribute(
                    self.map.get_position_map(Coordinates(x, y, 0)))
                if items is not None:
                    try:
                        if items.DataFactory.TypeFlag == TypeObject.FLOOR:
                            sprite_id = self.manager_object.get_sprite_id(items.DataFactory.NameSprite,
                                                                          items.DataFactory.Sprites)
                            if sprite_id is None:
                                continue
                            floor = Floor(Coordinates(x, y, 0), source_texture=sprite_id[0])
                            self.render_layers[1].append(floor)
                    except AttributeError as err:
                        print(items)

    def limit_size_execute(self):
        return [(self.size[0] / LIMIT_VIEW_X), (self.size[1] / LIMIT_VIEW_Y)]

    def draw_major(self, **kwargs):
        self.size = [kwargs.get("window")[0], kwargs.get("window")[1]]
        self.rectangle.size = self.size
        self.canvas.clear()
        for index in self.render_layers.keys():
            for elements in self.render_layers.get(index):
                elements.draw(
                    delta=kwargs.get("delta"),
                    limit_size=self.limit_size_execute(),
                    canvas=self.canvas)

    def update(self, *args):
        for index in self.render_layers.keys():
            for elements in self.render_layers.get(index):
                elements.update()
