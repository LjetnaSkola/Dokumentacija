from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal', spacing=20, padding=20)
        for i in range(1, 6):
            button = Button(text=f'Button {i}', size_hint_y=None, height=50, pos_hint={'center_y': 0.5})
            layout.add_widget(button)

        return layout


if __name__ == '__main__':
    MyApp().run()
