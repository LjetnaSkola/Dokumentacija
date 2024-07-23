from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2, rows=4)
        self.ime_input = TextInput(hint_text='Ime', multiline=False)
        self.prezime_input = TextInput(hint_text='Prezime', multiline=False)
        self.godine_input = TextInput(hint_text='Godine', multiline=False)
        self.ime = Label(text='Ime', font_size=20)
        self.prezime = Label(text='Prezime', font_size=20)
        self.godine = Label(text='Godine', font_size=20)
        self.rezultat = Label(text='', font_size=20)
        self.b1 = Button(text='Button 1')
        self.b1.bind(on_press=self.on_button_click)
        layout.add_widget(self.ime)
        layout.add_widget(self.ime_input)
        layout.add_widget(self.prezime)
        layout.add_widget(self.prezime_input)
        layout.add_widget(self.godine)
        layout.add_widget(self.godine_input)
        layout.add_widget(self.rezultat)
        layout.add_widget(self.b1)
        return layout


    def on_button_click(self, instance):
        user_input = "Ime: " +  self.ime_input.text + " Prezime: " + self.prezime_input.text + " Godine: " + self.godine_input.text
        self.rezultat.text = user_input


def main():
    MyApp().run()

    
if __name__ == "__main__":
    main()
