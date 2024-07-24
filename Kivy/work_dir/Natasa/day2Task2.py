from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

class MyButton(Button):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.text = "Button"

        with self.canvas.before:
            Color(0, 1, 0, 1)
            self.rect_before = Rectangle(pos=(100, 100), size=(200, 100))

        with self.canvas.after:
            Color(0, 0, 1, 0.5)
            self.rect_after = Rectangle(pos=(100, 100), size=(150, 150))

class CanvasExampleApp(App):
    def build(self):
        return MyButton(size_hint=(None, None), size=(200, 50), pos=(100, 100))

if __name__ == '__main__':
    CanvasExampleApp().run()