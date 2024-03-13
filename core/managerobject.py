from typing import Optional

from configuration.constants import DataIdentifier
from core.core import Core, ItemInternal, OutfitsInternal


class ManagerObject:
    def __init__(self, core: Core) -> None:
        self.core = core
        self._data = core.preparing_data_internal("data/data.json", DataIdentifier.DATA)
        self._items = core.preparing_data_internal("data/items.json", DataIdentifier.ITEMS)
        self._outfits = core.preparing_data_internal("data/outfits.json", DataIdentifier.OUTFITS)
        self.sprites = {}

        # load sprites in memory RAM
        self.load_data_sprite()

    def load_data_sprite(self) -> None:
        self.sprites.update(self.core.import_json_default("assets/floor.atlas"))
        self.sprites.update(self.core.import_json_default("assets/human.atlas"))

    def get_sprite_id(self, name_sprite, id_sprite: list):
        list_obj = []
        for id_items in id_sprite:
            if self.sprites.get(name_sprite, {}).get(str(id_items)) is None:
                return None
            list_obj.append("atlas://assets/%s/%s" % (name_sprite.split(".")[0], id_items))
        return list_obj

    def get_outfits_attribute(self, id_outfits) -> OutfitsInternal:
        internal: Optional[OutfitsInternal] = self._outfits.get(id_outfits)
        if internal is None:
            return None
        data = self._data.get(internal.DataFactory)
        if data is None:
            print(internal)
            print(data)
        internal.add_data_factory(data)
        return internal

    def get_items_attribute(self, id_items) -> ItemInternal:
        internal: Optional[ItemInternal] = self._items.get(id_items)
        if internal is None:
            return None
        internal.add_data_factory(self._data.get(internal.IDDataFactory))
        return internal
