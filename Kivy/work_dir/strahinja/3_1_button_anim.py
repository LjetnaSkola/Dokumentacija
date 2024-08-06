from kivy.uix.accordion import Animation
from kivy.app import App
from kivy.uix.widget import Widget


class MyRelative(Widget):
    def animate_top(self, c):
        Animation(
            x=500, background_color=(*c.background_color[:3], 0), duration=5
        ).start(c)

    def animate_bottom(self, c):
        anim_c = Animation(x=500, duration=5)
        anim_o = Animation(background_color=(*c.background_color[:3], 0.5), duration=1)
        anim_s = Animation(size=(tuple(map(lambda a: a * 2, c.size))), duration=1)
        anim = anim_c + anim_o + anim_s
        anim.start(c)


class BtnAnimApp(App):
    def build(self):
        return MyRelative()


if __name__ == "__main__":
    BtnAnimApp().run()
