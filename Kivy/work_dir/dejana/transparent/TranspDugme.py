from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyButton(Button):
    pass


class MyApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        button = MyButton()
        root.add_widget(button)
        return root


if __name__ == '__main__':
    MyApp().run()
