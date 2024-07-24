from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider

class DrawingWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.r = 0  # Default red value
        self.g = 0  # Default green value
        self.b = 1 # Default blue value

    def on_touch_down(self, touch):
        with self.canvas:
            Color(self.r, self.g, self.b)
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class PaintApp(App):
    def build(self):
        self.drawing_widget = DrawingWidget()

        # Sliders for RGB color selection
        self.red_slider = Slider(min=0, max=1, value=0)
        self.green_slider = Slider(min=0, max=1, value=0)
        self.blue_slider = Slider(min=0, max=1, value=1)

        # Bind sliders to update color
        self.red_slider.bind(value=self.update_color)
        self.green_slider.bind(value=self.update_color)
        self.blue_slider.bind(value=self.update_color)

        # Layout for sliders and drawing widget
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.drawing_widget)
        layout.add_widget(self.red_slider)
        layout.add_widget(self.green_slider)
        layout.add_widget(self.blue_slider)

        return layout

    def update_color(self, instance, value):
        self.drawing_widget.r = self.red_slider.value
        self.drawing_widget.g = self.green_slider.value
        self.drawing_widget.b = self.blue_slider.value

if __name__ == '__main__':
    PaintApp().run()
