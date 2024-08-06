from kivy.uix.progressbar import ProgressBar
from kivy.uix.slider import Slider
from kivy.uix.actionbar import Button
from kivy.uix.codeinput import TextInput
from kivy.uix.actionbar import Label
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.clock import Clock


class MyGrid(App):
    def build(self):
        self.box = GridLayout(rows=3)
        self.slider = Slider(min=0, max=50, step=1)
        self.box.add_widget(self.slider)

        self.progress = ProgressBar()
        self.box.add_widget(self.progress)

        Clock.schedule_interval(lambda dt: self.update_progress(), 10)

        self.concat = Label()
        self.box.add_widget(self.concat)
        return self.box

    def update_progress(self):
        self.progress.value = self.slider.value
        self.update_label()

    def update_label(self):
        self.concat.text = f"Slider value is {self.slider.value:.0f}"


if __name__ == "__main__":
    MyGrid().run()
