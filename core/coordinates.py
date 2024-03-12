
class Coordinates:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        
    def position(self, position):
        x = position[0]
        y = position[1]
        z = position[2]
        
    def __str__(self) -> str:
        return f"X: {self.x} Y: {self.y} Z: {self.z}"