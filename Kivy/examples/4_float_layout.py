from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class FloatLayoutExample(App):
    def build(self):
        layout = FloatLayout()

        # Button with fixed position
        btn1 = Button(text='Button 1', size_hint=(None, None))
        btn1.pos = (100, 200)  # Fixed position

        # Button with size_hint, adjusts size but not position
        btn2 = Button(text='Button 2', size_hint=(0.3, 0.2))
        btn2.pos = (300, 200)  # Fixed position

        layout.add_widget(btn1)
        layout.add_widget(btn2)

        return layout

if __name__ == '__main__':
    FloatLayoutExample().run()
