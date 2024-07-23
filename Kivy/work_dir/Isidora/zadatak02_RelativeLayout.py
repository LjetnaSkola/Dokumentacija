from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout


class RelativeLayoutApp(App):
    def build(self):
        layout = RelativeLayout()

        button1 = Button(text=f'Button 1', size_hint=(.2, .1), pos_hint={'x': 0, 'y': 0})
        button2 = Button(text=f'Button 2', size_hint=(.2, .1), pos_hint={'right': 1, 'y': 0})
        button3 = Button(text=f'Button 3', size_hint=(.2, .1), pos_hint={'right': 1, 'top': 1})
        button4 = Button(text=f'Button 4', size_hint=(.2, .1), pos_hint={'x': 0, 'top': 1})
        button5 = Button(text=f'Button 5', size_hint=(.2, .1), pos_hint={'center_x': .5, 'center_y': .5})
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        layout.add_widget(button5)

        return layout


if __name__ == '__main__':
    RelativeLayoutApp().run()
