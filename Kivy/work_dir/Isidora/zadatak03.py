from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class DisplayInfoApp(App):
    def build(self):
        self.layout = GridLayout(cols=2, rows=4, padding=10, spacing=10)

        self.layout.add_widget(Label(text='Name'))
        self.name_input = TextInput(multiline=False)
        self.layout.add_widget(self.name_input)

        self.layout.add_widget(Label(text='Surname'))
        self.surname_input = TextInput(multiline=False)
        self.layout.add_widget(self.surname_input)

        self.layout.add_widget(Label(text='Age'))
        self.age_input = TextInput(multiline=False)
        self.layout.add_widget(self.age_input)

        self.result_label = Label(text='The result will be displayed here')
        submit_button = Button(text='Submit')
        submit_button.bind(on_press=self.on_submit)
        self.layout.add_widget(submit_button)
        self.layout.add_widget(self.result_label)

        return self.layout

    def on_submit(self, instance):
        name = self.name_input.text
        surname = self.surname_input.text
        age = self.age_input.text
        result = f"Name: {name} Surname: {surname} Age: {age}"
        self.result_label.text = result


if __name__ == '__main__':
    DisplayInfoApp().run()
