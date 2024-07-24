from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = RelativeLayout()
        for i in range(1, 6):
            layout.add_widget(
                Button(
                    text=f"Button {i}", size_hint=(None, None), pos=(i * 100, i * 100)
                )
            )
        return layout


if __name__ == "__main__":
    MyApp().run()
