from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color


class MyButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(0, 1, 0, 1)
            Rectangle(pos=(200, 300))

        with self.canvas.after:
            Color(1, 0, 0, 0.5)
            Rectangle(pos=(150, 200))


class CanvasApp(App):
    def build(self):

        return MyButton(text="Button 1", size_hint=(None, None), size=(250, 100),
                        pos=(170, 250))


if __name__ == "__main__":
    CanvasApp().run()
