from core.managerobject import ManagerObject
from kivy.graphics import Rectangle
from core.core import Direction, OutfitsInternal
from typing import Optional

class Animation:
    def __init__(self, id_outfit:int, manager:ManagerObject, rectangle:Rectangle):
        self.__manager = manager
        self.direction_flag = Direction.SOUTH
        self.__outfits_internal : Optional[OutfitsInternal] = self.__manager.get_outfits_attribute(id_outfit)
        
        self.__direction_now = self.__outfits_internal.DataFactory.DirectionSprite[self.direction_flag][0]
        self.__content_direction_now = self.__outfits_internal.DataFactory.DirectionSprite[self.direction_flag]
        self.__movements = True
        self.rectangle= rectangle
        self.rectangle.source = self.__manager.get_sprite_outfits_id(self.__outfits_internal.DataFactory.NameSprite,
                                                                   self.__direction_now)
        self._animation_count = .0
        self._speed_animation = 8.0
        
    def set_movements(self, movements:bool) -> None:
        if not movements:
            self.__direction_now = self.__content_direction_now[0]
        self.__movements = movements
        
    def set_direction(self, direction:Direction) -> None:
        self.__content_direction_now = self.__outfits_internal.DataFactory.DirectionSprite[direction]
        self.__direction_now = self.__content_direction_now[0]
        
    def draw(self, **kwargs):
        dt : Optional[float] =  kwargs.get("delta")
        if self.__movements:
            self._animation_count += self._speed_animation * dt
            
            if self._animation_count >= 1:
                if int(self._animation_count )>= len(self.__content_direction_now):
                    self._animation_count = 0
                self.__direction_now = int(self._animation_count)
                name_id_sprite = self.__manager.get_sprite_outfits_id(self.__outfits_internal.DataFactory.NameSprite, self.__content_direction_now[int(self.__direction_now)])
                self.rectangle.source = name_id_sprite
            