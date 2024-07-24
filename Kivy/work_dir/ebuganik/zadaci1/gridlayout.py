import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class GridLayoutApp(App):
    def build(self):
        layout = GridLayout(cols=4, rows=2)
        layout.add_widget(Button(text = '1'))
        layout.add_widget(Button(text = '2'))
        layout.add_widget(Button(text = '3'))
        layout.add_widget(Button(text = '4'))
        layout.add_widget(Button(text = '5'))
        return layout

if __name__ == '__main__':
    GridLayoutApp().run()