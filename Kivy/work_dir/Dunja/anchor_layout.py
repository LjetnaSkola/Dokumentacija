from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout


class AnchorLayoutApp(App):
    def build(self):
        layout = AnchorLayout(anchor_x="right", anchor_y="bottom", padding=20)
        button = Button(text=f"Button 1", size_hint=(0.25, 0.75))
        layout.add_widget(button)

        button2 = Button(text=f"Button 2", size_hint=(0.5, 0.25))
        layout.add_widget(button2)

        return layout


if __name__ == "__main__":
    AnchorLayoutApp().run()
