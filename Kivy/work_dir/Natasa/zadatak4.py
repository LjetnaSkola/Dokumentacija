from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.clock import Clock

class MyBoxLayoutApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.slider = Slider(min=0, max=50, value=0, step=1)
        layout.add_widget(self.slider)

        self.progress_bar = ProgressBar(max=50)
        layout.add_widget(self.progress_bar)

        self.label = Label(text='Odabrana vrijednost: 0')
        layout.add_widget(self.label)

        Clock.schedule_once(self.update_progress_bar, 10)

        return layout

    def update_progress_bar(self, dt):

        selected_value = int(self.slider.value)
       
        self.progress_bar.value = selected_value
        self.label.text = f'Odabrana vrijednost: {selected_value}'

if __name__ == '__main__':
    MyBoxLayoutApp().run()
