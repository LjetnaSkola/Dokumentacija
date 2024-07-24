import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutApp(App):
    def build(self):
        hor_box = BoxLayout(orientation = 'vertical')
        hor_box.add_widget(Button(text = '1'))
        hor_box.add_widget(Button(text = '2'))
        hor_box.add_widget(Button(text = '3'))
        hor_box.add_widget(Button(text = '4'))
        hor_box.add_widget(Button(text = '5'))
        return hor_box

if __name__ == '__main__':
    BoxLayoutApp().run()