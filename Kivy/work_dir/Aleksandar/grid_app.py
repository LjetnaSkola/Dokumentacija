from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class GridApp(App):
    def build(self):
        layout = GridLayout(cols=2, rows=4, padding=10, spacing=10)

        # Row 1: Ime
        layout.add_widget(Label(text='Ime'))
        self.ime_input = TextInput(multiline=False)
        layout.add_widget(self.ime_input)

        # Row 2: Prezime
        layout.add_widget(Label(text='Prezime'))
        self.prezime_input = TextInput(multiline=False)
        layout.add_widget(self.prezime_input)

        # Row 3: Godine
        layout.add_widget(Label(text='Godine'))
        self.godine_input = TextInput(multiline=False)
        layout.add_widget(self.godine_input)

        # Row 4: Button and Result Label
        self.result_label = Label(text='Result is going to be displayed here.')
        self.submit_button = Button(text='Submit')
        self.submit_button.bind(on_press=self.on_button_press)
        layout.add_widget(self.result_label)
        layout.add_widget(self.submit_button)

        return layout

    def on_button_press(self,instance):
        ime = self.ime_input.text
        prezime = self.prezime_input.text
        godine = self.godine_input.text
        result_text = f'Ime {ime}, Prezime {prezime}, Godine {godine}'
        self.result_label.text = result_text


if __name__ == '__main__':
    GridApp().run()
