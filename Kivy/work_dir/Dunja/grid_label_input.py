from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class MyApp(App):
    def press_on_button(self, instance):
        first_name = self.fn_input.text
        last_name = self.ln_input.text
        age = self.a_input.text
        concatenated_text = f"Ime {first_name} Prezime {last_name} Godine {age}"
        self.label.text = concatenated_text

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fn_input = TextInput(multiline=False)
        self.ln_input = TextInput(multiline=False)
        self.a_input = TextInput(multiline=False)
        self.label = Label(text="", font_size='20sp')

    def build(self):
        layout = GridLayout(rows=4, cols=2)
        first_name = Label(text="Ime")
        last_name = Label(text="Prezime")
        age = Label(text="Godine")
        button = Button(text="Click!", font_size='20sp', color="red")
        button.bind(on_press=self.press_on_button)


        layout.add_widget(first_name)
        layout.add_widget(self.fn_input)
        layout.add_widget(last_name)
        layout.add_widget(self.ln_input)
        layout.add_widget(age)
        layout.add_widget(self.a_input)
        layout.add_widget(button)
        layout.add_widget(self.label)
        return layout


if __name__ == "__main__":
    MyApp().run()
