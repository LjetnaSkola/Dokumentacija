from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

class CustomButton(Button):
    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        self.text = "Test button"
        self.size_hint = (None, None)
        self.size = (200, 100)

        with self.canvas.before:
            self.color_before = Color(1, 0, 0, 1)
            self.rect_before = Rectangle(size=self.size, pos=self.pos)

        with self.canvas.after:
            self.color_after = Color(0, 0, 1, 0.1)
            self.rect_after = Rectangle(size=self.size, pos=self.pos)

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect_before.pos = self.pos
        self.rect_before.size = self.size
        self.rect_after.pos = self.pos
        self.rect_after.size = self.size


class ButtonCanvasApp(App):
    def build(self):
        return CustomButton(pos_hint={'center_x': 0.5, 'center_y': 0.5})


if __name__ == '__main__':
    ButtonCanvasApp().run()
