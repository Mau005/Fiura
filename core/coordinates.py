class Coordinates:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def get_position(self):
        return [self.x, self.y, self.x]

    def __str__(self) -> str:
        return f"X: {self.x} Y: {self.y} Z: {self.z}"
