from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class MyRelativeLayoutApp(App):
    def build(self):
        layout = RelativeLayout()

        for i in range(1, 6):
            button = Button(text=str(i),
                            size_hint=(None, None),
                            size=(100, 50),
                            pos_hint={'x': 0.1*i, 'y': 0.5})
            layout.add_widget(button)

        return layout

if __name__ == '__main__':
    MyRelativeLayoutApp().run()
