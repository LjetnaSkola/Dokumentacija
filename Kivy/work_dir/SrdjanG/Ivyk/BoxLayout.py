from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = BoxLayout()
        for i in range(1, 6):
            layout.add_widget(Button(text=f"Button {i}"))
        return layout


if __name__ == "__main__":
    MyApp().run()
