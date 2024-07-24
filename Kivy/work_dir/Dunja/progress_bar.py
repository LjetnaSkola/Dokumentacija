from kivy.app import App
from kivy.uix.progressbar import ProgressBar
from kivy.uix.slider import Slider
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import _usleep


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pb = ProgressBar(max=50)
        self.pb.value = 0
        self.slider = Slider(min=0, max=50, value=0, step=1)
        self.label = Label(text=f"Selected value: {self.slider.value}")

        self.slider.bind(on_touch_down=self.slider_changed)

    def slider_changed(self, touch, instance):
        _usleep(10000)
        self.pb.value = self.slider.value
        self.label.text = str(f"Selected value: {self.slider.value}")

    def build(self):
        layout = GridLayout(rows=2, cols=2)

        layout.add_widget(self.pb)
        layout.add_widget(self.slider)
        layout.add_widget(self.label)

        return layout


if __name__ == "__main__":
    MyApp().run()
