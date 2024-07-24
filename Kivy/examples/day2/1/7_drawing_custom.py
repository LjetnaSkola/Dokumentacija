from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line

class MyWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 0, 0)
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=2)

    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)

class CustomDrawingApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    CustomDrawingApp().run()
