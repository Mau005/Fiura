from typing import Optional

from kivy.graphics import Rectangle, Color
from kivy.uix.widget import Widget

from configuration.constants import KeyboardKey, LIMIT_VIEW_Y, LIMIT_VIEW_X, LIMIT_VIEW_PLAYER_X, \
    LIMIT_VIEW_PLAYER_Y, \
    TypeObject, \
    DirectionPlayer, Direction
from core.coordinates import Coordinates
from core.manager_object import ManagerObject
from entity.edge import Edge
from entity.floor import Floor
from entity.player import Player
from maps.map import Map
from core.core import ManagerDataInternal


class Render(Widget):
    def __init__(self, size_internal, configuration, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = [None, None]
        self.configuration = configuration
        self.load_map_complete = False
        self.size = size_internal
        self.manager_object = ManagerObject()
        self.player = Player(self.manager_object, 1, "KraynoDev",Coordinates(0, 0, 0), configuration=self.configuration)
        self.map = Map(100, 100)
        self.map.set_position_map(Coordinates(0, 0, 0), 4)
        self.map.set_position_map(Coordinates(1, 0, 0), 16)
        self.map.set_position_map(Coordinates(3, 0, 0), 16)
        self.map.set_position_map(Coordinates(4, 0, 0), 16)
        
        
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
        
        self.init_map()

    def init_map(self):
        coord = self.player.coord
        for x in range(self.map.get_len_map_x()):
            for y in range(self.map.get_len_map_y(x)):
                id_items = self.map.get_position_map(Coordinates(x, y, 0))
                item_factory: Optional[ManagerDataInternal] = self.manager_object.get_items_attribute(id_items)
                item = None
                x_target, y_target = 0,0
                if item_factory is None:
                    continue
                else:
                    x_target = x - coord.x + LIMIT_VIEW_PLAYER_X
                    y_target =  y - coord.y + LIMIT_VIEW_PLAYER_Y
                    
                if item_factory.data_factory.type_object == TypeObject.FLOOR:
                    item = Floor(self.manager_object, Coordinates(x_target, y_target, 0), item_factory, self.configuration)
                    self.render_layers[1].append(item)
                elif item_factory.data_factory.type_object == TypeObject.EDGES:
                    item = Edge(self.manager_object,Coordinates(x_target,y_target, 0), item_factory, self.configuration)
                    self.render_layers[2].append(item)
                elif item_factory.data_factory.type_object == TypeObject.OBJECT_SOLID:
                    item = Edge(self.manager_object,Coordinates(x_target, y_target, 0), item_factory,self.configuration)
                    self.render_layers[2].append(item)
                if item_factory.data_factory.collision:
                    self.collide.append(item)
                    
                self.add_widget(item)

        self.load_map_complete = True

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
        content = [0, Coordinates(0, 0, 0), Direction.NULL]
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
        status_col = False

        for elements in self.collide:
            if self.player.collider.collide_widget(elements.collider):
                if self.load_map_complete:
                    status_col = True
                
        
                
        if status_col:
            coord = Coordinates(0,0,0)
            delta = .025
            if self.player.animation.direction_flag  == Direction.WEST:
                self.player.movement(DirectionPlayer.EAST.value, delta)
                coord = DirectionPlayer.EAST.value
            elif self.player.animation.direction_flag  == Direction.EAST:
                self.player.movement(DirectionPlayer.WEST.value, delta)
                coord = DirectionPlayer.WEST.value
            elif self.player.animation.direction_flag  == Direction.NORTH:
                self.player.movement(DirectionPlayer.SOUTH.value, delta)
                coord = DirectionPlayer.SOUTH.value
            elif self.player.animation.direction_flag  == Direction.SOUTH:
                self.player.movement(DirectionPlayer.NORTH.value, delta)
                coord = DirectionPlayer.NORTH.value
            self.update_map(self.player.speed * delta, coord, **kwargs)
        else:
            speed, coord, _ = self.movements_player(set_keyboard, delta)
            self.update_map(speed, coord, **kwargs)
                


    def update_map(self, speed, coord, **kwargs):
        for index in self.render_layers.keys():
            for elements in self.render_layers.get(index):
                elements.update(player_cord=[speed, coord], **kwargs)
