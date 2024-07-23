from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        label = Label(text="Hello World!", font_size=100)
        label.size_hint = (1,1)
        # layout = BoxLayout(orientation='vertical')
        # layout.add_widget(label)
        return label


def main():
    MyApp().run()


if __name__ == "__main__":
    main()
