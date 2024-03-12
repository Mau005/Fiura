from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Fbo
from core.coordinates import Coordinates
from core.managerobject import ManagerObject
from core.core import Core
from maps.map import Map
from configuration.constants import TypeObject
from entity.floor import Floor
from configuration.constants import LIMIT_VIEW_Y, LIMIT_VIEW_X
import random


class Render(Widget):
    def __init__(self,window,  **kwargs):
        super().__init__(**kwargs)
        self.size_hint = [None, None]
        self.size = window
        self.core = Core()
        self.manager_object = ManagerObject(self.core)
        
        self.map = Map(100,100)
        for index in range(0, 10):
            self.map.set_position_map(Coordinates(random.randint(0, 10),random.randint(0, 10),random.randint(0, 10)), random.randint(0, 3),)

        self.render_layers = {
            1:[], #Floor
            2:[], #edge
            3:[], #object
            4:[], #entitys
            5:[] #object_upper
        }
        with self.canvas.before:
            #self.fbo = Fbo(size=self.size)
            self.rectangle = Rectangle(pos = self.pos, size= self.size)
            
        self.init_map()
        
            
    def init_map(self):
        for x in range(self.map.get_len_map_x()):
            for y in range(self.map.get_len_map_y(x)):
                items = self.manager_object.get_items_attribute(self.map.get_position_map(Coordinates(x,y,0)))
                if items is not None:
                    if items.object_internal.TypeFlag == TypeObject.FLOOR:
                        spriteId = self.manager_object.get_sprite_id(items.object_internal.NameSprite, items.object_internal.Sprites)
                        if spriteId is None:
                            continue
                        print(spriteId[0])
                        floor = Floor(Coordinates(x, y, 0), self.limit_size_execute(), source_texture=spriteId[0])
                        self.render_layers[1].append(floor)
                        
    def limit_size_execute(self):
        return [(self.size[0] / LIMIT_VIEW_X), (self.size[1] / LIMIT_VIEW_Y)]
            
    def draw_major(self, **kwargs):
        ##Actualizamos la ventana princial
        self.size = [kwargs.get("window")[0], kwargs.get("window")[1]]
        self.rectangle.size = self.size
        
        self.canvas.clear()
        ##actualizamos la lista de sprites
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
                