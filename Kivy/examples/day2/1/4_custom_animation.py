from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.animation import Animation

class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        with self.canvas:
            self.color = Color(1, 0, 0, 1)
            self.ellipse = Ellipse(pos=(100, 100), size=(50, 50))

    def animate(self):
        anim = Animation(pos=(300, 300), size=(100, 100), duration=10)
        anim.bind(on_progress=self.on_animation_progress)
        anim.start(self.ellipse)

    def on_animation_progress(self, animation, widget, progression):
        self.color.rgba = (1 - progression, progression, 0, 1)

class MyApp(App):
    def build(self):
        widget = MyWidget()
        widget.animate()
        return widget

if __name__ == '__main__':
    MyApp().run()
