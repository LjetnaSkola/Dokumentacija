from kivy.app import App
from kivy.uix.widget import Widget

class MyWidget(Widget):
    pass

class Canvas_ExampleApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Canvas_ExampleApp().run()