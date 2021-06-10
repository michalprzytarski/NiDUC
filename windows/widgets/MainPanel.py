from windows.widgets.ControlPanel import ControlPanel
from windows.widgets.InfoPanel import InfoPanel

import kivy
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.0.0')  # replace with your current kivy version !


# Panel wypełniający całe okno
class MainPanel(BoxLayout):

    def __init__(self, sim, sim_thread, **kwargs):
        super(MainPanel, self).__init__(**kwargs)

        self.control_panel = ControlPanel(sim, sim_thread)
        self.add_widget(self.control_panel)

        self.info_panel = InfoPanel(sim)
        self.add_widget(self.info_panel)
