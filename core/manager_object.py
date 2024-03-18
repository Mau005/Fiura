from typing import Optional

from configuration.constants import DataIdentifier, TypeObject
from core.core import ManagerDataInternal, OutfitsDataInternal, preparing_data_internal, import_json_default


class ManagerObject:
    def __init__(self) -> None:
        self._data = preparing_data_internal("data/data.json", DataIdentifier.DATA)
        self._items = preparing_data_internal("data/items.json", DataIdentifier.ITEMS)
        self._outfits = preparing_data_internal("data/outfits.json", DataIdentifier.OUTFITS)
        self.sprites = {}

        # load sprites in memory RAM
        self.load_data_sprite()

    def load_data_sprite(self) -> None:
        self.sprites.update(import_json_default("assets/floor.atlas"))
        self.sprites.update(import_json_default("assets/human.atlas"))
        self.sprites.update(import_json_default("assets/water_animation.atlas"))
        self.sprites.update(import_json_default("assets/edge_green.atlas"))

    def get_sprite_id(self, name_sprite, id_sprite):
        if self.sprites.get(name_sprite, {}).get(str(id_sprite)) is None:
            return None
        return "atlas://assets/%s/%s" % (name_sprite.split(".")[0], id_sprite)

    def get_outfits_attribute(self, id_outfits) -> OutfitsDataInternal:
        internal: Optional[OutfitsDataInternal] = self._outfits.get(id_outfits)
        if internal is None:
            raise Exception(f"Error load Outfits {id_outfits}")
        internal.add_data_factory(self._data.get(internal.id_data_factory))
        internal.data_factory.collision = True
        return internal

    def exist_items_attribute(self, id_items) -> TypeObject:
        if id_items in self._items.keys():
            return self._data.get(self._items.get(id_items).id_data_factory).type_object
        return TypeObject.NULL

    def get_items_attribute(self, id_items) -> ManagerDataInternal:
        internal: Optional[ManagerDataInternal] = self._items.get(id_items)
        if internal is None:
            return None
        internal.add_data_factory(self._data.get(internal.id_data_factory))
        return internal
