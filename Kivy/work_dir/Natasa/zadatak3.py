from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayoutApp(App):
    def build(self):
    
        layout = GridLayout(cols=2, rows=4, spacing=10, padding=10)

        labels = ['Ime:', 'Prezime:', 'Godine:']
        self.inputs = []

        for label_text in labels:
            layout.add_widget(Label(text=label_text))
            text_input = TextInput(multiline=False)
            self.inputs.append(text_input)
            layout.add_widget(text_input)

        self.result_label = Label(text='')
        layout.add_widget(self.result_label)

        button = Button(text='Prikaži rezultat', on_press=self.show_result)
        layout.add_widget(button)

        return layout

    def show_result(self, instance):
        
        ime = self.inputs[0].text
        prezime = self.inputs[1].text
        godine = self.inputs[2].text

        
        self.result_label.text = f'Ime: {ime} Prezime: {prezime} Godine: {godine}'

if __name__ == '__main__':
    MyGridLayoutApp().run()
