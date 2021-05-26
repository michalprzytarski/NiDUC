from windows.widgets.NumberPanelLabel import NumberPanelLabel
from windows.widgets.NumberPanelTextInput import NumberPanelTextInput

import kivy
from kivy.uix.gridlayout import GridLayout

kivy.require('2.0.0')  # replace with your current kivy version !

# Panel służący do wprowadzania wartości do InputText
class NumberPanel(GridLayout):
    def __init__(self, **kwargs):
        super(NumberPanel, self).__init__(**kwargs)

        # Dodanie styli do klasy
        self.cols = 2

        # Wprowadzanie ilości pracowników
        self.add_widget(NumberPanelLabel(text='Ilość pracowników: '))
        self.numberOfWorkersTextInput = NumberPanelTextInput()
        self.add_widget(self.numberOfWorkersTextInput)

        # Wprowadzanie ilości wózków widłowych
        self.add_widget(NumberPanelLabel(text='Ilość wózków widłowych: '))
        self.numberOfForkliftsTextInput = NumberPanelTextInput()
        self.add_widget(self.numberOfForkliftsTextInput)