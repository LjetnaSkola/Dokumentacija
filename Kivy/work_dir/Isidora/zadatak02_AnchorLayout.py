from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout


class AnchorLayoutApp(App):
    def build(self):
        layout = AnchorLayout(anchor_x='left', anchor_y='top')
        sublayout = GridLayout(cols=3, spacing=10)

        for i in range(5):
            button = Button(text=f'Button {i + 1}', size_hint=(None, None), size=(125, 75))
            sublayout.add_widget(button)

        layout.add_widget(sublayout)
        return layout


if __name__ == '__main__':
    AnchorLayoutApp().run()
