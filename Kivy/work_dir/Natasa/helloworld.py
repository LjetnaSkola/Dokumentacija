import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.label import Label

class MyLabelApp(App):
	def build(self):
		lbl = Label(text ="Hello World!")
		return lbl

label = MyLabelApp()
label.run()
