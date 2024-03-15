import random
from typing import Optional

from kivy.graphics import Rectangle
from kivy.uix.widget import Widget

from configuration.constants import LIMIT_VIEW_Y, LIMIT_VIEW_X, LIMIT_VIEW_PLAYER_X, LIMIT_VIEW_PLAYER_Y
from configuration.constants import TypeObject
from core.coordinates import Coordinates
from core.core import Core, ItemInternal, Direction
from core.managerobject import ManagerObject
from entity.floor import Floor
from entity.player import Player
from maps.map import Map


class Render(Widget):
    def __init__(self, size_internal, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = [None, None]
        self.size = size_internal
        self.core = Core()
        self.manager_object = ManagerObject(self.core)
        self.player = Player(self.manager_object, 1, Coordinates(0, 0, 0))
        self.map = Map(100, 100)
        self.map.set_position_map(Coordinates(0,0,0), 1)
        self.map.set_position_map(Coordinates(1,0,0), 2)
        self.map.set_position_map(Coordinates(2,0,0), 2)
        self.map.set_position_map(Coordinates(3,0,0), 2)
        

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
                            print("entra aca?")
                            self.add_widget(floor)
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
                
    def movements_player(self,key, dt):
        self.player.animation.set_movements(True)
        if 119 in key: #w
            self.player.animation.set_direction(Direction.NORTH)
            return self.player.movemens(Coordinates(0,1,0), dt)
        elif 97 in key: #a
            self.player.animation.set_direction(Direction.WEST)
            return self.player.movemens(Coordinates(-1,0,0), dt)
        elif 115 in key: #s
            self.player.animation.set_direction(Direction.SOUTH)
            return self.player.movemens(Coordinates(0,-1,0), dt)
        elif 100 in key: #d
            self.player.animation.set_direction(Direction.EAST)
            return self.player.movemens(Coordinates(1,0,0), dt)
        else:
            self.player.animation.set_movements(False)
            return [0, Coordinates(0,0,0)]

    def update(self, **kwargs):
        
        speed, coord  =self.movements_player(kwargs.get("keyboard"), kwargs.get("delta"))
        for index in self.render_layers.keys():
            for elements in self.render_layers.get(index):
                elements.update(player_cord=[speed, coord], **kwargs)

    def check_collisions(self):
        for obj1 in self.collidable_objects:
            for obj2 in self.collidable_objects:
                if obj1 != obj2 and self.check_collision(obj1, obj2):
                    print("Colisión detectada entre", obj1, "y", obj2)

    def check_collision(self, obj1, obj2):
        x1, y1, width1, height1 = obj1.collision_area
        x2, y2, width2, height2 = obj2.collision_area
        return x1 < x2 + width2 and x1 + width1 > x2 and y1 < y2 + height2 and y1 + height1 > y2
