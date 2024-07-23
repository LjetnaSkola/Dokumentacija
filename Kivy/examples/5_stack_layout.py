from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

class StackLayoutExample(App):
    def build(self):
        layout = StackLayout(size_hint=(0.6, 0.1), pos_hint={'center_x': 0.5, 'top': 1})
        for i in range(3):
            layout.add_widget(Button(text=f'Button {i}'))
        return layout

if __name__ == '__main__':
    StackLayoutExample().run()
