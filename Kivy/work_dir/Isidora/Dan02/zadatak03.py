from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.label import Label


class MyWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_color = [1, 0, 0, 1]  # Default to red with full opacity

    def on_touch_down(self, touch):
        # Check if touch is within MyWidget boundaries
        if self.collide_point(*touch.pos):
            with self.canvas:
                Color(*self.current_color)
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=2)

    def on_touch_move(self, touch):
        # Check if touch is within MyWidget boundaries
        if self.collide_point(*touch.pos):
            touch.ud['line'].points += (touch.x, touch.y)

    def set_color(self, r, g, b):
        self.current_color = [r, g, b, self.current_color[3]]

    def set_opacity(self, opacity):
        self.current_color[3] = opacity


class CustomDrawingApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        title_label = Label(text="Drawing App", font_size=25, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        drawing_area = MyWidget(size_hint=(1, 1))  # Ensure MyWidget takes available space

        color_selection_layout = BoxLayout(size_hint=(1, None), height=75)

        red_button = Button(text="Red", background_color=(1, 0, 0, 1))
        red_button.bind(on_press=lambda instance: drawing_area.set_color(1, 0, 0))

        green_button = Button(text="Green", background_color=(0, 1, 0, 1))
        green_button.bind(on_press=lambda instance: drawing_area.set_color(0, 1, 0))

        blue_button = Button(text="Blue", background_color=(0, 0, 1, 1))
        blue_button.bind(on_press=lambda instance: drawing_area.set_color(0, 0, 1))

        color_selection_layout.add_widget(red_button)
        color_selection_layout.add_widget(green_button)
        color_selection_layout.add_widget(blue_button)

        opacity_layout = BoxLayout(size_hint=(1, None), height=75)
        opacity_label = Label(text="Opacity")
        opacity_slider = Slider(min=0, max=1, value=1)
        opacity_slider.bind(value=lambda instance, value: drawing_area.set_opacity(value))

        opacity_layout.add_widget(opacity_label)
        opacity_layout.add_widget(opacity_slider)

        root.add_widget(title_label)
        root.add_widget(color_selection_layout)
        root.add_widget(opacity_layout)
        root.add_widget(drawing_area)

        return root


if __name__ == '__main__':
    CustomDrawingApp().run()
