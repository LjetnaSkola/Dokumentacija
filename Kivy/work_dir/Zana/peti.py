from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class ScrollableLabel(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout(cols=1, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.add_widget(self.layout)

    def add_label(self, text):
        label_text = f"Labela: {text[:5]}"
        self.layout.add_widget(Label(text=label_text))


class ItemApp(App):
    def build(self):
        self.scrollable_label = ScrollableLabel()

        self.item_label = Label(text="Item")
        self.text_input = TextInput(multiline=False)
        self.submit_button = Button(text="Submit")
        self.submit_button.bind(on_press=self.on_submit)

        layout = GridLayout(cols=2)
        layout.add_widget(self.item_label)
        layout.add_widget(self.text_input)
        layout.add_widget(self.submit_button)

        main_layout = GridLayout(cols=1)
        main_layout.add_widget(layout)
        main_layout.add_widget(self.scrollable_label)

        return main_layout

    def on_submit(self, instance):
        entered_text = self.text_input.text[:5]
        self.scrollable_label.add_label(entered_text)
        self.text_input.text = ""


if __name__ == '__main__':
    ItemApp().run()
