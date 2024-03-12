from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock

from entity.camera import Camera
from render.render import Render
from kivy.atlas import Atlas
from kivy.uix.button import Button


class MyGame(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.render = Render(Window.size)
        Clock.schedule_interval(self.update, 1 /60)
        Clock.schedule_interval(self.draw, 1/60)

    def draw(self, *args):
        self.render.draw_major(delta = args, window=Window.size)
        
    def update(self, *args):
        self.render.update(*args)
        
    def build(self):
        return self.render
    
    
if __name__ == "__main__":
    
    MyGame().run()