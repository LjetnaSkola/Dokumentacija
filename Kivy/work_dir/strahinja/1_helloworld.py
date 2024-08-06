from kivy.uix.actionbar import Label
from kivy.app import App


class MainApp(App):
    def build(self):
        return Label(text="Hello World!", font_size=50)


if __name__ == "__main__":
    MainApp().run()
