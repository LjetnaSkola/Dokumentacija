from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.animation import Animation

class MyLayout(RelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.button1 = Button(text='Top Left', size_hint=(None, None), size=(100, 50))
        self.button2 = Button(text='Botom Left', size_hint=(None, None), size=(100, 50))

        self.add_widget(self.button1)
        self.add_widget(self.button2)

        self.button1.pos_hint = {'x': 0, 'top': 1}
        self.button2.pos_hint = {'x': 0, 'y': 0}
        self.button1.bind(on_press=self.animate1)
        self.button2.bind(on_press=self.animate2)

    def animate1(self, instance):
        anim1 = Animation(pos_hint={'x': 0.2}, duration=4) & Animation(opacity=0, duration=4)
        anim1.start(instance)
        
    def animate2(self, instance):
        anim2 = Animation(pos_hint={'x': 0.2}, duration=5) + Animation(opacity=0.5, duration=2) + Animation(size=(200, 100))
        anim2.start(instance)
        


class MyApp(App):
    def build(self):
        return MyLayout()


def main():
    MyApp().run()

    
if __name__ == "__main__":
    main()
