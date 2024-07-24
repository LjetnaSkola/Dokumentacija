from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.graphics import Line, Color

    
class DrawingWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._touches = []

    def on_touch_down(self, touch):
        with self.canvas:
            Color(DrawingApp.red, DrawingApp.blue, DrawingApp.green)
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=2)
            self._touches.append(touch.ud['line'])

    def on_touch_move(self, touch):
        if 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]
            
    def clear_canvas(self):
        self.canvas.clear()
        self._touches = []


class DrawingApp(App):
    red = 1
    blue = 1
    green = 1
    def build(self):
        layout = RelativeLayout()
        self.red_slider = Slider(min=0, max=1, value=1, size=(100, 50), size_hint=(None, None))
        self.blue_slider = Slider(min=0, max=1, value=1, size=(100,50), size_hint=(None,None))
        self.green_slider = Slider(min=0, max=1, value=1, size=(100,50), size_hint=(None,None))
        self.red_slider.bind(value=self.update_red_slider)
        self.blue_slider.bind(value=self.update_blue_slider)
        self.green_slider.bind(value=self.update_green_slider)
        
        self.clear_button = Button(text='Clear', size_hint=(None, None), size=(100, 50))
        self.clear_button.bind(on_press=self.clear_canvas)

        drawer = DrawingWidget()
        layout.add_widget(drawer)
        box_layout = BoxLayout(orientation='vertical')
        box_layout.add_widget(self.red_slider)
        box_layout.add_widget(self.blue_slider)
        box_layout.add_widget(self.green_slider)
        box_layout.add_widget(self.clear_button)
        layout.add_widget(box_layout)
        
        return layout

    def update_red_slider(self, instance, value):
        DrawingApp.red = value
        
    def update_blue_slider(self, instance, value):
        DrawingApp.blue = value
        
    def update_green_slider(self, instance, value):
        DrawingApp.green = value
        
    def clear_canvas(self, instance):
        self.root.children[1].clear_canvas()
        
def main():
        DrawingApp().run()

    
if __name__ == "__main__":
    main()
