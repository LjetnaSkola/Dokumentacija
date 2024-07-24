from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.animation import Animation


class AnimatedButtonsApp(App):
    def build(self):
        layout = RelativeLayout()

        self.button1 = Button(text='Upside left', size_hint=(None, None), size=(200, 100))
        self.button2 = Button(text='Downside left', size_hint=(None, None), size=(200, 100))

        self.button1.bind(on_press=self.animate1)
        self.button2.bind(on_press=self.animate2)

        layout.add_widget(self.button1)
        layout.add_widget(self.button2)

        return layout

    def on_start(self):
        self.button1.pos = (0, self.root_window.height - self.button1.height)
        self.button2.pos = (0, 0)

    def animate1(self, instance):
        anim = Animation(x=200, opacity=0.5, duration=1)
        anim.start(instance)

    def animate2(self, instance):
        anim1 = Animation(x=200, duration=1)

        anim2 = Animation(opacity=0.5, size=(300, 150), duration=1)
        anim1 += anim2
        anim1.start(instance)


if __name__ == '__main__':
    AnimatedButtonsApp().run()
    