
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
class Collider:
    def __init__(self, size_father, collider = {"x": .2, "y": .2, "center":1},**kwargs):
        super().__init__(**kwargs)
        
        
        with self.canvas.before:
            Color(1,0,1)
            self.rectangle = Rectangle()
        