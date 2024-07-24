from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.animation import Animation
from kivy.graphics import Rectangle, Color

class MyApp(App):
    def build(self):
        layout = RelativeLayout()

        with layout.canvas.before:
            Color(1, 0.8, 0.2, 0.94)
            self.rect_below = Rectangle(size_hint=(None,None), size=(300, 50), pos=(305, 299))
        
        self.button = Button(text="BUTTON!", size_hint=(None,None), size=(200, 100),
                             pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        def update_rectangle_position(instance, value):
            new_pos = (layout.width, layout.height)
            self.rect_below.pos = new_pos

        self.button.bind(size=update_rectangle_position)
        
        with layout.canvas.after:
            Color(0.198, 0.265, 0.346, 0.67)
            self.rect_below = Rectangle(opacity=0.4, size_hint=(None,None), size=(180, 200), pos=(300, 299))
        
        layout.add_widget(self.button)
        return layout


def main():
    MyApp().run()

    
if __name__ == "__main__":
    main()
