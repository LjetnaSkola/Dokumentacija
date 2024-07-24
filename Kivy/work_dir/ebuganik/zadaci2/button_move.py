from kivy.app import App
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.relativelayout import RelativeLayout
class ButtonMovementApp(App):
    def animate_b1(self, instance):
        # Animation for button 1
        anim = Animation(x=100, opacity=0, duration=1)
        anim += Animation(x=0, opacity=1, duration=1)
        anim.start(instance)

    def animate_b2(self, instance):
        # Animation for button 2
        anim = Animation(x=100, opacity=0, duration=1)
        anim += Animation(x=0, opacity=1, duration=1)
        anim += Animation(size_hint=(.4, .4), duration=1)
        anim.start(instance)

    def build(self):
        layout = RelativeLayout()
        # Button in top left corner
        button1 = Button(size_hint=(.2, .2), pos_hint={'left': 1, 'top': 1}, text='1')
        button1.bind(on_press=self.animate_b1)
        layout.add_widget(button1)
        # Button in bottom left corner
        button2 = Button(size_hint=(.2, .2), pos_hint={'left': 1, 'bottom': 1}, text='2')
        button2.bind(on_press=self.animate_b2)
        layout.add_widget(button2)

        return layout

if __name__ == '__main__':
    ButtonMovementApp().run()