from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.slider import Slider
from kivy.clock import Clock


class DisplaySliderValueApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.info_label = Label(text='After every 10 seconds, the slider value is displayed in the label below!')
        self.layout.add_widget(self.info_label)

        self.label = Label(text='Value of the slider will be displayed here after 10 seconds')
        self.layout.add_widget(self.label)

        self.progress_bar = ProgressBar(max=10)
        self.layout.add_widget(self.progress_bar)

        self.slider = Slider(min=0, max=50, value=0)
        self.layout.add_widget(self.slider)

        self.progress_bar_value = 0
        Clock.schedule_interval(self.update_progress_bar, 1)

        return self.layout

    def update_progress_bar(self, dt):
        if self.progress_bar_value < 10:
            self.progress_bar_value += 1
            self.progress_bar.value = self.progress_bar_value
        else:
            self.progress_bar_value = 0  # Reset progress bar
            self.progress_bar.value = self.progress_bar_value
            self.display_slider_value()

    def display_slider_value(self):
        slider_value = self.slider.value
        self.label.text = f'The slider value is: {slider_value}'


if __name__ == '__main__':
    DisplaySliderValueApp().run()
