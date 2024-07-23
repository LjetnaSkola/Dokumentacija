from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.clock import Clock

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        self.slider = Slider(min=0, max=50, value=25, step=1)
        self.progress_bar = ProgressBar(max=50)
        self.label = Label(text='Trenutna vrijednost:')
        layout.add_widget(self.slider)
        layout.add_widget(self.progress_bar)
        layout.add_widget(self.label)

        Clock.schedule_interval(self.update_progress, 10)

        return layout

    def update_progress(self, dt):
        value = int(self.slider.value)
        self.progress_bar.value = value

        self.label.text = f'Trenutna vrijednost: {value}'

if __name__ == '__main__':
    MyApp().run()
