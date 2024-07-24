from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Rectangle, Ellipse


class MyWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            # Draw a line from (100, 100) to (300, 300)
            Line(points=[100, 100, 300, 300], width=2)

            # Draw a rectangle with top-left at (400, 100) and size (200, 100)
            Rectangle(pos=(400, 100), size=(200, 100))

            # Draw an ellipse with center at (250, 400) and radius (100, 50)
            Ellipse(pos=(150, 350), size=(200, 100))

class GraphicsApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    GraphicsApp().run()
