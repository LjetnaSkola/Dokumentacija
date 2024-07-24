from kivy.animation import Animation
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button


class ButtonApp(App):
    def on_button_press1(self, instance):
        anim = Animation(pos_hint={'x': 0.5}, duration=1)
        anim &= Animation(opacity=0, duration=5)
        anim.start(instance)

    def on_button_press2(self, instance):
        anim = Animation(pos_hint={'x': 0.5}, duration=1)
        anim += Animation(opacity=0, duration=5)
        anim &= Animation(size=(600, 250), duration=3)
        anim.start(instance)

    def build(self):
        layout = RelativeLayout()
        btn1 = Button(text="Button 1", size_hint=(None, None), size=(300, 250), pos_hint={'x': 0, 'top': 1})
        btn2 = Button(text="Button 2", size_hint=(None, None), size=(300, 250), pos_hint={'x': 0, 'y': 0})

        btn1.bind(on_press=self.on_button_press1)
        btn2.bind(on_press=self.on_button_press2)

        layout.add_widget(btn1)
        layout.add_widget(btn2)

        return layout


if __name__ == "__main__":
    ButtonApp().run()