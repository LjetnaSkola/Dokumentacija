from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import Rectangle

class MyWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            # Draw a background image
            self.bg_image = Image(source='example.jpg')
            Rectangle(texture=self.bg_image.texture, pos=self.pos, size=(800, 600))

class GraphicsApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    GraphicsApp().run()
