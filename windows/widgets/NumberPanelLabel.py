import kivy
from kivy.uix.label import Label

kivy.require('2.0.0')  # replace with your current kivy version !

# klasa używana do stylizowania Label w panelu ControlGridPanel
class NumberPanelLabel(Label):
    def __init__(self, **kwargs):
        super(NumberPanelLabel, self).__init__(**kwargs)

        # Dodanie styli do klasy
        self.text_size = (self.width, None)
        self.halign = 'center'