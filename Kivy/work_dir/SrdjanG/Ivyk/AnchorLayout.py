from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = AnchorLayout(anchor_x="left", anchor_y="bottom", padding=10)
        for i in range(1, 6):
            layout.add_widget(
                Button(text=f"Button {i}", size_hint=(None, None), pos=(i * 10, i * 10))
            )
        return layout


if __name__ == "__main__":
    MyApp().run()
