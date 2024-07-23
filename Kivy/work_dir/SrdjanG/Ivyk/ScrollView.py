from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        self.layout = GridLayout(cols=1)
        self.layout.add_widget(Label(text="Item:"))

        self.text_input = TextInput()
        self.layout.add_widget(self.text_input)

        self.submit_button = Button(text="Submit")
        self.submit_button.bind(on_press=self.on_submit)
        self.layout.add_widget(self.submit_button)

        self.scroll_view = ScrollView()
        self.layout.add_widget(self.scroll_view)

        self.grid_inside_scroll = GridLayout(cols=1, size_hint_y=None)
        self.grid_inside_scroll.bind(
            minimum_height=self.grid_inside_scroll.setter("height")
        )
        self.scroll_view.add_widget(self.grid_inside_scroll)
        return self.layout

    def on_submit(self, instance):
        uneseni_tekst = self.text_input.text[:5]
        nova_labela = Label(
            text=f"Labela: {uneseni_tekst}", size_hint_y=None, height=40
        )
        self.grid_inside_scroll.add_widget(nova_labela)


if __name__ == "__main__":
    MyApp().run()
