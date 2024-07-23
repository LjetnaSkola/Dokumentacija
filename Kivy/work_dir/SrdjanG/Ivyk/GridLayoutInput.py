from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyApp(App):
    def build(self):
        layout = GridLayout(rows=4, cols=2)
        layout.add_widget(Label(text="Ime"))
        self.imeInput = TextInput()
        layout.add_widget(self.imeInput)

        layout.add_widget(Label(text="Prezime"))
        self.prezimeInput = TextInput()
        layout.add_widget(self.prezimeInput)

        layout.add_widget(Label(text="Godine"))
        self.godineInput = TextInput()
        layout.add_widget(self.godineInput)

        self.inputLayer = Label(text="")
        layout.add_widget(self.inputLayer)
        b1 = Button(text="Unesi")
        b1.bind(on_press=self.input)
        layout.add_widget(b1)

        return layout

    def input(self, instance):
        self.inputLayer.text = f"Ime {self.imeInput.text} Prezime {self.prezimeInput.text} Godine {self.godineInput.text}"


if __name__ == "__main__":
    MyApp().run()
