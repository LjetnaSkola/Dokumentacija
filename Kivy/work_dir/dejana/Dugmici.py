from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation


class MyLayout(FloatLayout):
    def on_button1_release(self, instance):
        anim = Animation(pos=(120, self.height - 120), opacity=0.5, duration=1)
        anim.start(instance)

    def on_button2_release(self, instance):
        anim = Animation(pos=(120, 20), opacity=1, duration=1)
        anim += Animation(pos=(120, 20), opacity=0.5, duration=1)
        anim += Animation(size=(200, 100), duration=1)
        anim.start(instance)


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()
