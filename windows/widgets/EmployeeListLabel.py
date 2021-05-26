import kivy
from kivy.uix.label import Label
#  from kivy.graphics import Canvas, Color, Rectangle
kivy.require('2.0.0')  # replace with your current kivy version !

# klasa uzywana do stylizowania informacji o pracowniku
class EmployeeListLabel(Label):
    def __init__(self, **kwargs):
        super(EmployeeListLabel, self).__init__(**kwargs)

        self.size_hint_y = None
        self.height = self.texture_size[1]
        self.text_size = (self.width, None)
        self.padding = (2, 2)
        #with self.canvas:
            # Add a red color
            #Color(1., 0, 0)

            # Add a rectangle
            #Rectangle(pos=self.pos, size=self.size)
        #self.canvas = Canvas()
        #self.canvas.(1, 1, 1)
        #    Rectangle(pos=self.pos, size=self.size)