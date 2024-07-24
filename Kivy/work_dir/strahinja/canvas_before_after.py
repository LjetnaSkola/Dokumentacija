from kivy.uix.accordion import ObjectProperty
from kivy.uix.accordion import Animation
from kivy.app import App
from kivy.uix.widget import Widget


class MyRelative(Widget):
    btn = ObjectProperty()

    def __init__(self, **kwargs):
        super(MyRelative, self).__init__(**kwargs)


class CanvasBeforeAfterApp(App):
    def build(self):
        return MyRelative()


if __name__ == "__main__":
    CanvasBeforeAfterApp().run()
