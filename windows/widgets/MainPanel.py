from windows.widgets.ControlPanel import ControlPanel
from windows.widgets.InfoPanel import InfoPanel

import kivy
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.0.0')  # replace with your current kivy version !

# Panel wypełniający całe okno
class MainPanel(BoxLayout):

    def __init__(self, sim, **kwargs):
        super(MainPanel, self).__init__(**kwargs)

        #  self.size = (self.root.width, self.root.height)
        #  self.background_color = (1, 0, 0, 1)

        self.control_panel = ControlPanel(sim)
        self.add_widget(self.control_panel)

        self.info_panel = InfoPanel(sim)
        self.add_widget(self.info_panel)