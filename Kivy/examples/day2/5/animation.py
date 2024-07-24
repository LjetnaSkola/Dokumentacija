from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.core.window import Window

Window.size = (720, 400)

class MyLayout(Widget):
   def animating(self, widget, *args):
      animate = Animation(
         pos=(widget.pos[0], Window.height - 50)
      )
      animate += Animation(pos=(widget.pos[0], 0))
      animate += Animation(
         background_color=(0, 0, 1, 1),
         duration=1
      )
      animate += Animation(size_hint=(1, 1))
      animate += Animation(size_hint=(.5, .5))
      animate += Animation(pos_hint={"center_x": 0.1})
      animate += Animation(pos_hint={"center_x": 0.5})
      animate.start(widget)
      
      # Create a callback
      animate.bind(on_complete=self.my_callback)
   
   def my_callback(self, *args):
      self.ids.my_label.text = "Hello Kivy"

class AnimationApp(App):
   def build(self):
      return MyLayout()

if __name__ == '__main__':
   AnimationApp().run()