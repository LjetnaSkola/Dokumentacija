from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.effects.dampedscroll import DampedScrollEffect

class MyApp(App):
    def build(self):
        root_layout = StackLayout(padding=20, spacing=30)
        row = GridLayout(cols=2, rows=1, size_hint_y=None)
        self.grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scrollview = ScrollView(do_scroll_x=False, do_scroll_y=True)
        self.scrollview.add_widget(self.grid)
        self.item = Label(text="Item")
        self.text_input = TextInput(hint_text="Enter name", multiline=False)
        self.button = Button(text="Submit", size_hint_y=None)
        self.button.bind(on_press=self.on_button_pressed)
        row.add_widget(self.item)
        row.add_widget(self.text_input)
        root_layout.add_widget(row)
        root_layout.add_widget(self.button)
        root_layout.add_widget(self.scrollview)
        return root_layout

    def on_button_pressed(self, instance):
        text = ""
        if len(self.text_input.text) > 5:
            text = self.text_input.text[:5]
        else:
            text = self.text_input.text
        label = Label(text=f"Label: {text}", size_hint_y=None, height=40)
        self.grid.add_widget(label)


def main():
    MyApp().run()

    
if __name__ == "__main__":
    main()
