from kivy.uix.actionbar import Button
from kivy.uix.codeinput import TextInput
from kivy.uix.actionbar import Label
from kivy.uix.gridlayout import GridLayout
from kivy.app import App


class MyGrid(App):
    def build(self):
        self.box = GridLayout(rows=4, cols=2)
        self.box.add_widget(Label(text="First Name:"))
        self.fname = TextInput()
        self.box.add_widget(self.fname)
        self.box.add_widget(Label(text="Last Name:"))
        self.lname = TextInput()
        self.box.add_widget(self.lname)
        self.box.add_widget(Label(text="Age:"))
        self.age = TextInput()
        self.box.add_widget(self.age)

        self.concat = Label()
        self.box.add_widget(
            Button(text="Update label", on_press=lambda instance: self.update_label())
        )
        self.box.add_widget(self.concat)
        return self.box

    def update_label(self):
        self.concat.text = (
            f"{self.fname.text} {self.lname.text} is {self.age.text} years old"
        )


if __name__ == "__main__":
    MyGrid().run()
