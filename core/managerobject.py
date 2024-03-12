from core.core import Core

from configuration.constants import DataIdentifier
from entity.objects import ItemsInternal

class ManagerObject:
    def __init__(self, core:Core) -> None:
        self.core = core
        self._data =  core.preparing_data_internal("data/data.json", DataIdentifier.DATA)
        self._items = core.preparing_data_internal("data/items.json", DataIdentifier.ITEMS)
        
        self.sprites = {}
        
        #load sprites in memory RAM
        self.load_data_sprite()
        
    def load_data_sprite(self) ->None:
        self.sprites.update(self.core.import_json_default("assets/floor.atlas"))
        
    def get_sprite_id(self, name_sprite, id_sprite:list):
        list_obje = []
        for idItems in id_sprite:
            if self.sprites.get(name_sprite, {}).get(str(idItems)) == None:
                return None
            list_obje.append("atlas://assets/%s/%s" % (name_sprite.split(".")[0], idItems))
       
        return list_obje
        
        
    def get_items_attribute(self, id_items) -> ItemsInternal:
        internal = self._items.get(id_items)
        if internal is None:
            return None
        internal.object_internal = self._data.get(internal.DataFactory)
        return internal
        
        