from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2, rows=5, spacing=10)

        labels = ['Ime:', 'Prezime:', 'Godine:']
        self.text_inputs = []
        for label_text in labels:
            layout.add_widget(Label(text=label_text))
            text_input = TextInput(multiline=False)
            self.text_inputs.append(text_input)
            layout.add_widget(text_input)

        self.result_label = Label(text='')
        layout.add_widget(self.result_label)
        button = Button(text='Prikaži rezultat')
        button.bind(on_press=self.show_result)
        layout.add_widget(button)
        return layout

    def show_result(self, instance):

        ime = self.text_inputs[0].text
        prezime = self.text_inputs[1].text
        godine = self.text_inputs[2].text

        result_text = f'Ime {ime} Prezime {prezime} Godine {godine}'
        self.result_label.text = result_text

if __name__ == '__main__':
    MyApp().run()
