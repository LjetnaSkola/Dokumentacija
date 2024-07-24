from kivy.app import App
from kivy.properties import ListProperty
from kivy.graphics import Line, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class DrawingWidget(BoxLayout):
    current_color = ListProperty([1, 1, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lines = []

    def on_touch_down(self, touch):
        if self.ids.draw_space.collide_point(*touch.pos):
            with self.ids.draw_space.canvas.after:
                color = Color(*self.current_color, mode='rgb')
                line = Line(points=(touch.x, touch.y), width=2)
                self.lines.append((line, color))
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.lines and self.ids.draw_space.collide_point(*touch.pos):
            self.lines[-1][0].points += [touch.x, touch.y]
        return super().on_touch_move(touch)

    def update_color(self, *args):
        for line, color in self.lines:
            color.rgba = self.current_color + [1]


class DrawingApp(App):
    def build(self):
        return DrawingWidget()


if __name__ == '__main__':
    DrawingApp().run()
