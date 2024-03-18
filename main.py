from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.config import Config

from render.render import Render

from configuration.configuration import Configuration


class MyGame(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.configuration = Configuration()
        Config.set('graphics', 'width', self.configuration.resolution[0])
        Config.set('graphics', 'height', self.configuration.resolution[1])
        # Desactivar la capacidad de redimesnsionamiento
        Config.set('graphics', 'resizable', False)
        
        # TODO: Error android al tomor el teaclado Window.request_keyboard(self.on_keyboard_close, self, "text")
        Window.bind(on_key_down=self.on_keyboard_down)
        Window.bind(on_key_up=self.on_keyboard_up)
        self.size_internal = Window.size
        self.render = Render(self.size_internal)
        
        
        Clock.schedule_interval(self.update, 1 / 60)
        Clock.schedule_interval(self.draw, 1 / 60)
        self.key = set()

    def on_keyboard_down(self, *args):
        self.key.add(args[1])

    def on_keyboard_up(self, *args):
        self.key.discard(args[1])

    def on_keyboard_close(self, *args):
        pass

    def movements_keyboard(self, dt):
        pass

    def draw(self, *args):
        self.size_internal = Window.size
        self.render.draw_major(delta=args[0], window=self.size_internal)

    def update(self, *args):
        self.title = f"Pos X: {self.render.player.coord.x} Pos Y: {self.render.player.coord.y}"
        self.render.update(delta=args[0], keyboard=self.key)

    def build(self):
        return self.render


if __name__ == "__main__":
    game = MyGame()
    game.run()
