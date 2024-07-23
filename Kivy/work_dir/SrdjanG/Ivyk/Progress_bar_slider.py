from kivy.app import App
from kivy.uix.progressbar import ProgressBar
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock


class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical")
        self.slider = Slider(min=0, max=50, value=0)
        self.slider.bind(value=self.change_value)

        self.bar = ProgressBar(max=50)

        self.label = Label(text="")

        self.layout.add_widget(self.slider)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.bar)
        return self.layout

    def change_value(self, instance, value):
        self.label.text = f"Vrijedost: {int(value)}"

    def update_progress_bar(self, dt):
        slider_value = self.slider.value
        self.bar.value = slider_value

    def on_start(self):
        Clock.schedule_once(self.update_progress_bar, 10)


if __name__ == "__main__":
    MyApp().run()
