from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class GridLayoutApp(App):
    def build(self):
        layout = GridLayout(cols=3, padding=20)
        for i in range(5):
            button = Button(text=f"Button {i + 1}")
            layout.add_widget(button)
        return layout


if __name__ == "__main__":
    GridLayoutApp().run()
