import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock


class SliderProgressApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Slider Value: 25", size_hint_y=None, height=50)
        # Create a slider with range 0 to 50
        self.slider = Slider(min=0, max=50, value=25, step=1)
        # Create a progress bar
        self.progress = ProgressBar(max=100, value=0)
        # Bind the slider value change to update label
        self.slider.bind(value=self.on_slider_value_change)
        # Add widgets to the layout
        layout.add_widget(self.label)
        layout.add_widget(self.slider)
        layout.add_widget(self.progress)
        # Schedule the update_progress_bar function after 10 seconds
        Clock.schedule_once(self.update_progress_bar, 10)
        self.concat = Label()
        layout.add_widget(self.concat)
        return layout

    def on_slider_value_change(self, instance, value):
        self.label.text = f"Slider Value: {int(value)}"
    def update_progress_bar(self, dt):
        # Update progress bar value with current slider value
        self.progress.value = self.slider.value
        self.update_label()
    def update_label(self):
        self.concat.text = f"Progressbar value: {self.progress.value:.0f}"

if __name__ == '__main__':
    SliderProgressApp().run()
