from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout


class CustomButton(Button):
    pass


class CustomButtonApp(App):
    def build(self):
        return CustomButton()


if __name__ == '__main__':
    CustomButtonApp().run()
