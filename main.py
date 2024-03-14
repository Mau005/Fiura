from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from core.core import Direction
from core.coordinates import Coordinates
from render.render import Render



class MyGame(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #TODO: Error android al tomor el teaclado Window.request_keyboard(self.on_keyboard_close, self, "text")
        Window.bind(on_key_down=self.on_keyboard_down)
        Window.bind(on_key_up=self.on_keyboard_up)
        self.size_internal = Window.size
        self.render = Render(self.size_internal)
        Clock.schedule_interval(self.update, 1 / 60)
        Clock.schedule_interval(self.draw, 1 / 60)
        
        self.key = set()
        
    def on_keyboard_down(self, *args):
        self.key.add(args[1])
        print(f"Apreto tecla {args}")
        pass
    
    def on_keyboard_up(self, *args):
        self.key.discard(args[1])
        print(f"suelto Tecla {args}")
        pass
    
    def on_keyboard_close(self, *args):
        pass#Window.unbind(on_key_down=self.on_keyboard_down)
        #Window.unbind(on_key_up=self.on_keyboard_up)
        
    def movements_keyboard(self, dt):
        pass

    def draw(self, *args):
        self.size_internal = Window.size
        self.render.draw_major(delta=args[0], window=self.size_internal)

    def update(self, *args):
        self.render.update(delta=args[0], keyboard=self.key)

    def build(self):
        return self.render


if __name__ == "__main__":
    game = MyGame()
    game.run()
