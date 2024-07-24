from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Line
from kivy.uix.widget import Widget

class DrawingArea(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_color = None  

    def on_touch_down(self, touch):
        if self.current_color: 
            with self.canvas:
                Color(*self.current_color)
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=2)

    def on_touch_move(self, touch):
        if 'line' in touch.ud and self.current_color:
            touch.ud['line'].points += (touch.x, touch.y)

    def set_pen_color(self, color):
        self.current_color = color

class MyBoxLayoutApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='horizontal', padding=20, spacing=10)
        
        sliders_layout = BoxLayout(orientation='vertical', spacing=10)

        self.sliders = []
        self.progress_bars = []
        self.labels = []

        for i in range(3):
            slider = Slider(min=0, max=1, value=0, step=0.01)
            slider.bind(value=lambda instance, value, index=i: self.slider_changed(value, index))
            self.sliders.append(slider)
            sliders_layout.add_widget(slider)

            progress_bar = ProgressBar(max=1)
            self.progress_bars.append(progress_bar)
            sliders_layout.add_widget(progress_bar)

            label = Label(text=f'Odabrana vrijednost {i+1}: 0.00')
            self.labels.append(label)
            sliders_layout.add_widget(label)

        main_layout.add_widget(sliders_layout)

        # Dodavanje prostora za crtanje olovkom
        drawing_area = DrawingArea()
        main_layout.add_widget(drawing_area)

        # Dugme za postavljanje boje olovke
        set_color_button = Button(text='Postavi boju olovke')
        set_color_button.bind(on_press=self.set_pen_color_to_sliders)
        sliders_layout.add_widget(set_color_button)

        self.drawing_area = drawing_area

        return main_layout

    def slider_changed(self, value, index):
        self.progress_bars[index].value = value
        self.labels[index].text = f'Odabrana vrijednost {index+1}: {value:.2f}'

    def set_pen_color_to_sliders(self, instance):
        r = self.sliders[0].value
        g = self.sliders[1].value
        b = self.sliders[2].value
        self.drawing_area.set_pen_color((r, g, b))

if __name__ == '__main__':
    MyBoxLayoutApp().run()
