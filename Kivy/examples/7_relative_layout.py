from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class RelativeLayoutExample(App):
    def build(self):
        layout = RelativeLayout()

        # Button with position relative to layout
        btn1 = Button(text='Top Left', size_hint=(None, None), size=(100, 50))
        btn1.pos_hint = {'x': 0, 'y': 0.9}  # Relative position

        # Button with position relative to the center
        btn2 = Button(text='Center', size_hint=(None, None), size=(100, 50))
        btn2.pos_hint = {'center_x': 0.5, 'center_y': 0.5}  # Centered

        # Button with position relative to the bottom
        btn3 = Button(text='Below Center', size_hint=(None, None), size=(100, 50))
        btn3.pos_hint = {'center_x': 0.5, 'y': 0.1}  # Relative position

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)

        return layout

if __name__ == '__main__':
    RelativeLayoutExample().run()
