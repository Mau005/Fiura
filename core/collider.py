
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from configuration.configuration import Configuration

class Collider(Widget):
    def __init__(self, percentage_x_pos, percentage_y_pos, quad_percentage_x, quad_percentage_y , configuration:Configuration, color=(1,0,1), **kwargs):
        super().__init__(**kwargs)
        self.configuration = configuration
        self.percentage_x_pos = percentage_x_pos
        self.percentage_y_pos = percentage_y_pos
        self.quad_percentage_x = quad_percentage_x
        self.quad_percentage_y = quad_percentage_y
        
        with self.canvas.before:
            if self.configuration.debug:
                Color(color[0],color[1],color[2], .5)
                self.rectangle = Rectangle(pos=self.pos, size=self.size)
            
    def draw(self,pos_feather, size_feather, **kwargs):
        limit_size = kwargs.get("limit_size")
        pos_feather_new = [pos_feather[0], pos_feather[1]]
        pos_feather_new[0] += limit_size[0] * self.percentage_x_pos
        pos_feather_new[1] += limit_size[1] * self.percentage_y_pos
        
        size_feather_new = [size_feather[0], size_feather[1]]
        size_feather_new[0] = limit_size[0] * self.quad_percentage_x
        size_feather_new[1] = limit_size[1] * self.quad_percentage_y
        self.pos = pos_feather_new
        self.size = size_feather_new
        if self.configuration.debug:
            self.rectangle.pos = self.pos
            self.rectangle.size = self.size
            
    def update(self, **kwargs):
        pass
    
    
        