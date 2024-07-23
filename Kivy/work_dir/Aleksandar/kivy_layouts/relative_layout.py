from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button


class RelativeLayoutApp(App):
    def build(self):
        layout = RelativeLayout()
        for i in range(1, 6):
            button = Button(text=f'Button {i}', size_hint=(None, None), size=(100, 50), pos_hint={'x': i*0.1, 'y': i*0.1})
            layout.add_widget(button)
        return layout


if __name__ == '__main__':
    RelativeLayoutApp().run()
