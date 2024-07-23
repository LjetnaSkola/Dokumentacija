from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button


class AnchorLayoutApp(App):
    def build(self):
        layout = AnchorLayout()
        for i in range(1, 6):
            button = Button(text=f'Button {i}', size_hint=(None, None), size=(100, 50))
            layout.add_widget(button)
        return layout


if __name__ == '__main__':
    AnchorLayoutApp().run()
