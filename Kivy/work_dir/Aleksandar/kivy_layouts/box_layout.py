from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class BoxLayoutApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        for i in range(1, 6):
            button = Button(text=f'Button {i}')
            layout.add_widget(button)
        return layout


if __name__ == '__main__':
    BoxLayoutApp().run()
