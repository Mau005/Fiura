from maps.map import Map
from core.coordinates import Coordinates
from configuration.constants import LIMIT_VIEW_PLAYER_X, LIMIT_VIEW_PLAYER_Y, LIMIT_VIEW_X, LIMIT_VIEW_Y

mapa = Map(10,10)

player= Coordinates(0,1,0)


for x in range(0, mapa.get_len_map_x):
    for y in range( 0, mapa.get_len_map_y(x)):
        

