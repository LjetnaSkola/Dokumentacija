from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.core.window import Window


class TwoButtonsAnimationApp(App):
    def build(self):
        layout = RelativeLayout()

        self.top_left_button = Button(
                                    text="Top Left",
                                    size_hint=(None, None),
                                    size=(150, 75),
                                    pos=(0, Window.height - 75)
                                )
        self.top_left_button.bind(on_press=self.animate_top_left_button)
        layout.add_widget(self.top_left_button)

        self.bottom_left_button = Button(
                                        text="Bottom Left",
                                        size_hint=(None, None),
                                        size=(150, 75),
                                        pos=(0, 0)
                                )
        self.bottom_left_button.bind(on_press=self.animate_bottom_left_button)
        layout.add_widget(self.bottom_left_button)

        return layout

    def animate_top_left_button(self, instance):
        anim = Animation(pos=(350, Window.height - 75), duration=2) & Animation(opacity=0.5, duration=2)
        anim.start(instance)

    def animate_bottom_left_button(self, instance):
        anim = Animation(pos=(350, 0), duration=2) + Animation(opacity=0.5, duration=2) + Animation(size=(300, 150), duration=2)
        anim.start(instance)


if __name__ == '__main__':
    TwoButtonsAnimationApp().run()
