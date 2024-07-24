from kivy.app import App
from kivy.uix.button import Button
from kivy.animation import Animation

class MyButtonApp(App):
    def build(self):
        button = Button(text='Click Me!')
        button.bind(on_press=self.on_button_press)
        return button

    def on_button_press(self, instance):
        # Animation with callbacks
        anim = Animation(opacity=0, duration=7)
        anim.bind(on_start=self.on_animation_start, on_complete=self.on_animation_complete)
        anim.start(instance)

    def on_animation_start(self, instance, animation):
        print('Animation started!')

    def on_animation_complete(self, instance, animation):
        print('Animation completed!')

if __name__ == '__main__':
    MyButtonApp().run()
