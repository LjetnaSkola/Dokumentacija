from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation

class MyButtonApp(App):
    def build(self):
        layout = FloatLayout()
        button = Button(text='Click Me!', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button.bind(on_press=self.on_button_press)
        layout.add_widget(button)
        return layout

    def on_button_press(self, instance):
        # Create an animation to change the button's size and opacity
        anim = Animation(size=(200, 100), opacity=0, duration=5)
        anim.start(instance)

if __name__ == '__main__':
    MyButtonApp().run()
