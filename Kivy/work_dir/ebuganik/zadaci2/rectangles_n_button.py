from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

#Builder.load_file('canvas_example.kv')
class AwesomeButton(Widget):
    pass

class Canvas_ExampleApp(App):
    def build(self):
        return AwesomeButton()

if __name__ == '__main__':
    Canvas_ExampleApp().run()