from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

class ProgressSliderApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.slider = Slider(min=0, max=50, value=25)
        layout.add_widget(self.slider)

        self.progress_bar = ProgressBar(max=10)
        layout.add_widget(self.progress_bar)

        self.result_label = Label(text='Value will be displayed here.')
        layout.add_widget(self.result_label)

        self.start_button = Button(text='Start')
        self.start_button.bind(on_press=self.start_progress)
        layout.add_widget(self.start_button)

        return layout

    def start_progress(self, instance):
        self.progress_bar.value = 0
        Clock.schedule_interval(self.update_progress, 1)

    def update_progress(self, dt):
        if self.progress_bar.value < self.progress_bar.max:
            self.progress_bar.value += 1
        else:
            Clock.unschedule(self.update_progress)
            self.value = self.slider.value
            self.result_label.text = f'Slider value {self.value:.2f}'


if __name__ == '__main__':
    ProgressSliderApp().run()
