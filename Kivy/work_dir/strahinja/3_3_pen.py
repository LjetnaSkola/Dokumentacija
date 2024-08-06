from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.graphics import Color, Rectangle, Line


class MyRelative(BoxLayout):
    def __init__(self, **kwargs):
        super(MyRelative, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.rgb_layout = BoxLayout(size_hint_y=None, height=50)
        self.red_input = TextInput(
            hint_text="R",
            input_filter="int",
            multiline=False,
            size_hint_x=None,
            width=50,
        )
        self.green_input = TextInput(
            hint_text="G",
            input_filter="int",
            multiline=False,
            size_hint_x=None,
            width=50,
        )
        self.blue_input = TextInput(
            hint_text="B",
            input_filter="int",
            multiline=False,
            size_hint_x=None,
            width=50,
        )
        self.red_slider = Slider(min=0, max=255)
        self.green_slider = Slider(min=0, max=255)
        self.blue_slider = Slider(min=0, max=255)

        self.rgb_layout.add_widget(self.red_input)
        self.rgb_layout.add_widget(self.red_slider)
        self.rgb_layout.add_widget(self.green_input)
        self.rgb_layout.add_widget(self.green_slider)
        self.rgb_layout.add_widget(self.blue_input)
        self.rgb_layout.add_widget(self.blue_slider)

        self.add_widget(self.rgb_layout)
        self.canvas_widget = Widget(size_hint_y=None, height=500)
        self.add_widget(self.canvas_widget)

        self.current_color = (1, 0, 0, 1)

        with self.canvas_widget.canvas.before:
            self.bg_color = Color(*self.current_color)
            self.bg_rect = Rectangle(
                size=self.canvas_widget.size, pos=self.canvas_widget.pos
            )

        self.red_input.bind(text=self.update_color_from_text)
        self.green_input.bind(text=self.update_color_from_text)
        self.blue_input.bind(text=self.update_color_from_text)

        self.red_slider.bind(value=self.update_color_from_slider)
        self.green_slider.bind(value=self.update_color_from_slider)
        self.blue_slider.bind(value=self.update_color_from_slider)

    def update_color_from_text(self, instance, value):
        self.update_color()
        self.update_sliders()

    def update_color_from_slider(self, instance, value):
        self.update_color()
        self.update_text_inputs()

    def update_color(self):
        try:
            r = (
                int(self.red_input.text) / 255.0
                if self.red_input.text
                else self.red_slider.value / 255.0
            )
            g = (
                int(self.green_input.text) / 255.0
                if self.green_input.text
                else self.green_slider.value / 255.0
            )
            b = (
                int(self.blue_input.text) / 255.0
                if self.blue_input.text
                else self.blue_slider.value / 255.0
            )
            self.current_color = (r, g, b, 1)
            if hasattr(self, "bg_color"):
                self.bg_color.rgba = self.current_color
        except ValueError:
            pass

    def update_sliders(self):
        if hasattr(self, "red_slider"):
            self.red_slider.value = (
                int(self.red_input.text) if self.red_input.text else 0
            )
        if hasattr(self, "green_slider"):
            self.green_slider.value = (
                int(self.green_input.text) if self.green_input.text else 0
            )
        if hasattr(self, "blue_slider"):
            self.blue_slider.value = (
                int(self.blue_input.text) if self.blue_input.text else 0
            )

    def update_text_inputs(self):
        if hasattr(self, "red_input"):
            self.red_input.text = str(int(self.red_slider.value))
        if hasattr(self, "green_input"):
            self.green_input.text = str(int(self.green_slider.value))
        if hasattr(self, "blue_input"):
            self.blue_input.text = str(int(self.blue_slider.value))

    def on_touch_down(self, touch):
        if self.canvas_widget.collide_point(*touch.pos):
            self.start_draw(touch)
            return True
        return super(MyRelative, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.canvas_widget.collide_point(*touch.pos):
            self.continue_draw(touch)
            return True
        return super(MyRelative, self).on_touch_move(touch)

    def start_draw(self, touch):
        with self.canvas_widget.canvas:
            Color(*self.current_color)
            self.line = Line(points=[touch.x, touch.y], width=2)

    def continue_draw(self, touch):
        if hasattr(self, "line"):
            self.line.points += [touch.x, touch.y]


class PenApp(App):
    def build(self):
        return MyRelative()


if __name__ == "__main__":
    PenApp().run()
