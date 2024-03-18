from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup

Builder.load_file("handler/sprite_editor.kv")


def generate_atlas(nameFIle, size_x, size_y, quad_x, quad_y):
    normalize = {}
    count_x = size_x / quad_x
    count_y = size_y / quad_y
    aux = 0
    for x in range(0, int(count_x)):
        for y in range(0, int(count_y)):
            aux += 1
            normalize.update({str(aux): [x * quad_x, y * quad_y, quad_x, quad_y]})

    return {
        nameFIle: normalize
    }


class PopOptional(Popup):
    def __init__(self, function_internal, **kwargs):
        super(PopOptional, self).__init__(**kwargs)
        self.ids.load_button.bind(on_press=function_internal)


class FileChooserPopup(Popup):
    def __init__(self, function_submit, **kwargs):
        super(FileChooserPopup, self).__init__(**kwargs)
        self.size_hint = (0.9, 0.9)
        self.file_chooser = FileChooserListView()
        self.file_chooser.path = "./"
        self.file_chooser.filters = ["*.png", "*.jpg", "*.jpeg"]
        self.file_chooser.bind(on_submit=function_submit)
        self.file_chooser.bind(on_submit=self.dismiss_popup)
        self.file_chooser.bind(on_cancel=self.dismiss_popup)
        self.content = self.file_chooser

    def dismiss_popup(self, instance, *args):
        self.dismiss()


class Scene(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_name = None
        self.name_primitive = ""
        self.image = None
        self.size_pop = PopOptional(self.on_load_file)
        self.data = {}

    def on_execute_left_menu(self, *args):
        data = self.data.get(self.name_primitive)
        for key in data.keys():
            self.ids.container_atributes.add_widget(Button(text=key, size_hint_y=None, height=40))

    def open_file(self):
        file = FileChooserPopup(self.processing_load_file)
        file.open()

    def on_load_file(self, *args):
        self.name_primitive = self.file_name.split("/")[-1]
        self.data = generate_atlas(
            self.name_primitive,
            self.image.texture_size[0],
            self.image.texture_size[1],
            int(self.size_pop.ids.size_x.text),
            int(self.size_pop.ids.size_y.text),
        )
        self.ids.img_rect.texture = self.image.texture
        self.ids.img_rect.size = self.ids.container.size

        self.on_execute_left_menu()

    def processing_load_file(self, *args):
        self.file_name = args[1][0]
        self.image = Image(source=self.file_name)
        self.size_pop.open()


class SpriteEditor(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Scene()


if __name__ == "__main__":
    SpriteEditor().run()
