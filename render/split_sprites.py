
from kivy.atlas import Atlas
class SpriteSheet:
    
    def __init__(self, file_path) -> None:
        self.collections = Atlas(file_path)
        
        