from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock


class SliderApp(App):
    def build(self):
        layout = BoxLayout(padding=30, orientation='vertical')
        self.slider = Slider(min=0, max=50, value=25)
        self.slider_value = 25
        self.slider.bind(value=self.update_value)
        self.text_label = Label(text='', font_size=20)
        self.progress_bar = ProgressBar(max=100)
        layout.add_widget(self.slider)
        layout.add_widget(self.progress_bar)
        layout.add_widget(self.text_label)
        Clock.schedule_interval(self.update_progress, 1.0/33)
        Clock.schedule_once(self.progress_complete, 10)
        return layout

    def update_value(self, instance, value):
        self.slider_value = value
        
    def update_progress(self, dt):
        if self.progress_bar.value >= self.progress_bar.max:
            return False
        self.progress_bar.value += 0.30303030303    
        
    def progress_complete(self, dt):
        self.text_label.text = "Slider value: " + str(int(self.slider_value))


if __name__ == '__main__':
    SliderApp().run()
