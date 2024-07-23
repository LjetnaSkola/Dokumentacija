import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyLabelApp(App):
    def build(self):
        label = Label(text = "Hello World!")
        return label

lbl = MyLabelApp()
lbl.run()