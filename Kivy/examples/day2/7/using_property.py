from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

class MyWidget(BoxLayout):
    value = NumericProperty(0)

    def __init__(self, **kwargs):
       super(MyWidget, self).__init__(**kwargs)
       self.bind(value=self.on_value_change)

    def on_value_change(self, instance, value):
       print("Value changed " + str(value))

class PropertyApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    PropertyApp().run()