from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line


class MyWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = Color(1, 0, 0)

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.color.rgb)
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=2)

    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)


class DrawingApp(App):
    def build(self):
        layout = RelativeLayout()

        self.slider = Slider(min=1, max=3, value=1, step=1, size_hint=(None, None), size=(600, 100), pos_hint={'center_x': 0.5, 'top': 1})
        self.slider.bind(value=self.on_slider_value_change)
        layout.add_widget(self.slider)

        self.my_widget = MyWidget(pos=(0, 200))
        layout.add_widget(self.my_widget)
        return layout

    def on_slider_value_change(self, instance, value):
        if value == 1:
            self.my_widget.color = Color(1, 0, 0)  # Crvena boja
        elif value == 2:
            self.my_widget.color = Color(0, 1, 0)  # Zelena boja
        elif value == 3:
            self.my_widget.color = Color(0, 0, 1)  # Plava boja


if __name__ == "__main__":
    DrawingApp().run()
