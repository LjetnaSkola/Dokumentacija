from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window


class HelloWorldApp(App):

    def build(self):
        Window.size = (400, 200)
        label = Label(text='Hello, World!', font_size='24sp')
        return label


if __name__ == '__main__':
    HelloWorldApp().run()
