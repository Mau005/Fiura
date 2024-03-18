from kivy.graphics import Rectangle
from kivy.uix.widget import Widget

from core.coordinates import Coordinates
from core.core import TypeFlag
from kivy.uix.label import Label
from configuration.configuration import Configuration
from typing import Optional
from core.collider import Collider
from core.core import DataFactory
class Entity(Widget):
    def __init__(self, coordinates: Coordinates, name="", source_texture=None, configuration: Optional[Configuration] = None, data_factory:Optional[DataFactory]=None, **kwargs):
        super().__init__(**kwargs)
        self.data_factory = data_factory
        self._flag = TypeFlag.NULL
        self.configuration = configuration
        self.size_hint = [None, None]
        self.coord = coordinates if coordinates is not None else Coordinates(0, 0, 0)
        self.collision = False
        
        self.name = name
        self.label_name = Label(text=name, size_hint=[None, None])
        with self.canvas:
            self.rectangle = Rectangle(size=self.size, pos=self.pos, source=source_texture if source_texture is not None else "")
    
        self.collider =  Collider(0,0, 1, 1, self.configuration, color= (1,0,0) if self.data_factory.collision else (0,.8,0))
        self.add_widget(self.collider)
        self.add_widget(self.label_name)

    @property
    def flag(self):
        return self._flag

    @flag.setter
    def flag(self, flag):
        self._flag = flag

    def draw(self, **kwargs):
        limit_size = kwargs.get("limit_size")
        if not (self.flag == TypeFlag.PLAYER):
            self.pos = [self.coord.x * limit_size[0], self.coord.y * limit_size[1]]

        self.rectangle.size = limit_size
        self.rectangle.pos = self.pos
        self.size = limit_size
        
        
        self.collider.draw(self.pos, self.size, **kwargs)
        
        if self.flag == TypeFlag.ENEMY or self.flag == TypeFlag.NPC or self.flag == TypeFlag.PLAYER:
            self.label_name.pos = [self.pos[0], self.pos[1] +(limit_size[0]*0.3)]
            self.label_name.size = self.size
            
        kwargs.get("canvas").add(self.canvas)
        
            
        
        

    def draw_square(self, **kwargs):
        pass

    def movement(self, coord, speed):
        if coord.x > 0:
            self.coord.x -= speed
        if coord.x < 0:
            self.coord.x += speed
        if coord.y > 0:
            self.coord.y -= speed
        if coord.y < 0:
            self.coord.y += speed

    def update(self, **kwargs):
        
        if not (self.flag == TypeFlag.PLAYER):
            speed, coord = kwargs.get("player_cord")
            self.movement(coord, speed)
        pass
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print("Soy yo", touch.pos)

