from core.coordinates import Coordinates


class Map:

    def __init__(self, x, y) -> None:
        self._map = [[0] * x for _ in range(y)]

    def get_position_map(self, coord: Coordinates) -> list:
        return self._map[coord.x][coord.y]

    def set_position_map(self, coord: Coordinates, id_object: int) -> None:
        self._map[coord.x][coord.y] = id_object

    def get_len_map_x(self):
        return len(self._map)

    def get_len_map_y(self, x):
        return len(self._map[x])
