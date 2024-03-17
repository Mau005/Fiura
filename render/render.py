from typing import Optional

from kivy.graphics import Rectangle
from kivy.uix.widget import Widget

from configuration.constants import KeyboardKey, LIMIT_VIEW_Y, LIMIT_VIEW_X, LIMIT_VIEW_PLAYER_X, \
    LIMIT_VIEW_PLAYER_Y, \
    TypeObject, \
    DirectionPlayer, Direction
from core.coordinates import Coordinates
from core.managerobject import ManagerObject
from entity.edge import Edge
from entity.floor import Floor
from entity.player import Player
from maps.map import Map


class Render(Widget):
    def __init__(self, size_internal, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = [None, None]
        self.size = size_internal
        self.manager_object = ManagerObject()
        self.player = Player(self.manager_object, 1, Coordinates(0, 0, 0))
        self.map = Map(100, 100)
        self.map.set_position_map(Coordinates(2, 2, 0), 16)
        self.collide = []

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
        self.add_widget(self.player)
        self.init_map()

    def init_map(self):
        coord = self.player.coord
        for x in range(self.map.get_len_map_x()):
            for y in range(self.map.get_len_map_y(x)):
                id_items = self.map.get_position_map(Coordinates(x, y, 0))
                type_object: Optional[TypeObject] = self.manager_object.exist_items_attribute(id_items)
                item = None
                if type_object == TypeObject.NULL:
                    continue
                elif type_object == TypeObject.FLOOR:
                    item = Floor(self.manager_object, id_items,
                                 Coordinates(x - coord.x + LIMIT_VIEW_PLAYER_X, y - coord.y + LIMIT_VIEW_PLAYER_Y,
                                             0))
                    self.render_layers[1].append(item)
                elif type_object == TypeObject.EDGES:
                    item = Edge(self.manager_object, id_items,
                                Coordinates(x - coord.x + LIMIT_VIEW_PLAYER_X, y - coord.y + LIMIT_VIEW_PLAYER_Y, 0),
                                type_object)
                    self.render_layers[2].append(item)
                elif type_object == TypeObject.OBJECT_SOLID:
                    item = Edge(self.manager_object, id_items,
                                Coordinates(x - coord.x + LIMIT_VIEW_PLAYER_X, y - coord.y + LIMIT_VIEW_PLAYER_Y,
                                            0), type_object)
                    self.collide.append(item)
                    self.render_layers[2].append(item)
                self.add_widget(item)

    def limit_size_execute(self):
        return [(self.size[0] / LIMIT_VIEW_X), (self.size[1] / LIMIT_VIEW_Y)]

    def draw_major(self, **kwargs):
        self.size = [kwargs.get("window")[0], kwargs.get("window")[1]]
        self.rectangle.size = self.size
        self.canvas.clear()
        for index in self.render_layers.keys():
            if index == 4:
                self.player.draw(
                    delta=kwargs.get("delta"),
                    limit_size=self.limit_size_execute(),
                    canvas=self.canvas)

            for elements in self.render_layers.get(index):
                elements.draw(
                    delta=kwargs.get("delta"),
                    limit_size=self.limit_size_execute(),
                    canvas=self.canvas)

    def movements_player(self, key: list, dt):
        self.player.animation.set_movements(True)
        content = [0, Coordinates(0, 0, 0), None]
        if KeyboardKey.W.value in key:  # w
            content = self.player.movement(DirectionPlayer.NORTH.value, dt)
        elif KeyboardKey.A.value in key:  # a
            content = self.player.movement(DirectionPlayer.WEST.value, dt)
        elif KeyboardKey.S.value in key:  # s
            content = self.player.movement(DirectionPlayer.SOUTH.value, dt)
        elif KeyboardKey.D.value in key:  # d
            content = self.player.movement(DirectionPlayer.EAST.value, dt)
        else:
            self.player.animation.set_movements(False)

        return content

    def update(self, **kwargs):
        set_keyboard = kwargs.get("keyboard")
        delta = kwargs.get("delta")

        speed, coord, flag_direction = self.movements_player(set_keyboard, delta)

        for elements in self.collide:
            if self.player.collide_widget(elements):
                x = self.player.right + 5 >= elements.x
                if x:
                    if flag_direction is not None and flag_direction.EAST == Direction.EAST:
                        coord = DirectionPlayer.WEST.value

        self.update_map(speed, coord, **kwargs)

    def update_map(self, speed, coord, **kwargs):
        for index in self.render_layers.keys():
            for elements in self.render_layers.get(index):
                elements.update(player_cord=[speed, coord], **kwargs)
