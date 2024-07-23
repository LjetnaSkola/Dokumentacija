from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = GridLayout(rows=3, cols=3)
        for i in range(1, 6):
            layout.add_widget(Button(text=f"Button {i}"))
        return layout


if __name__ == "__main__":
    MyApp().run()
