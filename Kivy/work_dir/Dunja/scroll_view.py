from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        self.layout_inner = BoxLayout(orientation="vertical", size_hint_y=None)

        self.label = Label(text="Item", size_hint=(None, None), size=(200, 50))
        self.input = TextInput(size_hint=(None, None), size=(700, 50), multiline=False)
        self.submit = Button(text="Submit", size_hint=(1, None))

        self.submit.bind(on_press=self.press_on_button)

    def press_on_button(self, instance):
        lab = Label(text=self.input.text[:5])
        self.layout_inner.add_widget(lab)

    def build(self):
        self.layout.add_widget(self.layout_inner)

        self.layout_inner.add_widget(self.label)
        self.layout_inner.add_widget(self.input)
        self.layout_inner.add_widget(self.submit)

        return self.layout


if __name__ == "__main__":
    MyApp().run()
