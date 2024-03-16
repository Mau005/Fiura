from typing import Optional

from kivy.graphics import Rectangle

from configuration.constants import TypeObject
from core.core import Direction, OutfitsDataInternal, ManagerDataInternal
from core.managerobject import ManagerObject


class Animation:
    def __init__(self, id_sprite: int, manager: ManagerObject, rectangle: Rectangle,
                 type_obj: Optional[TypeObject] = TypeObject.FLOOR):
        self.__manager = manager
        self.direction_flag = Direction.SOUTH
        if type_obj == TypeObject.OUTFITS:
            self.__object_internal: Optional[OutfitsDataInternal] = self.__manager.get_outfits_attribute(id_sprite)
        else:
            self.__object_internal: Optional[ManagerDataInternal] = self.__manager.get_items_attribute(id_sprite)
        self.__direction_now = self.__object_internal.data_factory.direction_sprite[self.direction_flag][0]
        self.__content_direction_now = self.__object_internal.data_factory.direction_sprite[self.direction_flag]
        self.__movements = True
        self.rectangle = rectangle
        self.rectangle.source = self.__manager.get_sprite_outfits_id(self.__object_internal.data_factory.name_sprite,
                                                                     self.__direction_now)
        self._animation_count = .0
        self._speed_animation = 8.0

    def set_movements(self, movements: bool) -> None:
        if not movements:
            self.__direction_now = self.__content_direction_now[0]
        self.__movements = movements

    def set_direction(self, direction: Direction) -> None:
        self.__content_direction_now = self.__object_internal.data_factory.direction_sprite[direction]
        self.__direction_now = self.__content_direction_now[0]

    def draw(self, **kwargs):
        if not self.__object_internal.data_factory.status_animation:
            return
        dt: Optional[float] = kwargs.get("delta")
        if self.__movements:
            self._animation_count += self._speed_animation * dt

            if self._animation_count >= 1:
                if int(self._animation_count) >= len(self.__content_direction_now):
                    self._animation_count = 0
                self.__direction_now = int(self._animation_count)
                name_id_sprite = self.__manager.get_sprite_outfits_id(self.__object_internal.data_factory.name_sprite,
                                                                      self.__content_direction_now[
                                                                          int(self.__direction_now)])
                self.rectangle.source = name_id_sprite
