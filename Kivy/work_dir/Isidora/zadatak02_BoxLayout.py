from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        for i in range(5):
            button = Button(text=f'Button {i + 1}')
            layout.add_widget(button)

        return layout


if __name__ == '__main__':
    BoxLayoutApp().run()
