from kivy.uix.actionbar import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.settings import text_type
from kivy.uix.actionbar import Button
from kivy.uix.dropdown import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.actionbar import Label
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.clock import Clock


class MyGrid(App):
    def build(self):
        self.box = GridLayout(rows=2, cols=2)
        self.item = Label(text="Item")
        self.box.add_widget(self.item)

        self.input = TextInput()
        self.box.add_widget(self.input)

        self.button = Button(text="Dodaj labelu", on_press=lambda _: self.add_label())
        self.box.add_widget(self.button)

        self.scroll = ScrollView()
        self.stack = BoxLayout(orientation="vertical")
        self.scroll.add_widget(self.stack)
        self.box.add_widget(self.scroll)

        return self.box

    def add_label(self):
        self.stack.add_widget(Label(text=f"Labela: {self.input.text[0:5]}"))


if __name__ == "__main__":
    MyGrid().run()
