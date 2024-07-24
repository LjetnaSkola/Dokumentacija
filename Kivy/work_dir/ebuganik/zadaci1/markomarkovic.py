import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
class TutorialApp(App):
    def build(self):
        layout = GridLayout(cols=2, rows=4, spacing=10)
        self.labels = []
        self.inputs = []

        # Adding labels and text inputs for Name, Surname and Years
        for label_name in ['Name:', 'Surname:', 'Years:']:
            label = Label(text=label_name)
            input_text = TextInput(multiline=False)
            self.labels.append(label)
            self.inputs.append(input_text)

            layout.add_widget(label)
            layout.add_widget(input_text)

        # Adding button
        self.result_label = Label(text="")
        button = Button(text='Concatenated:', on_press=self.on_button_click)
        layout.add_widget(button)
        layout.add_widget(self.result_label)

        return layout

    def on_button_click(self, instance):
        # Get text from input
        name = self.inputs[0].text
        surname = self.inputs[1].text
        years = self.inputs[2].text

        # Concatenate strings and display
        result = f"Name: {name} Surname: {surname} Years: {years}"
        self.result_label.text = result

if __name__ == '__main__':
    TutorialApp().run()
