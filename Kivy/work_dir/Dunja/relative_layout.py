from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button


class RelativeLayoutApp(App):
    def build(self):
        layout = RelativeLayout()
        button = Button(text=f"Button 1", size_hint=(.25, .5), pos=(20, 20))
        layout.add_widget(button)

        button = Button(text=f"Button 2", size_hint=(.5, .25), pos=(500, 500))
        layout.add_widget(button)
        return layout


if __name__ == "__main__":
    RelativeLayoutApp().run()
