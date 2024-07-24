from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window

Window.size = (720, 400)

class AnchorLayoutExample(App):
   def build(self):
      lo = AnchorLayout(
         anchor_x='left', anchor_y='bottom'
      )
      self.l1 = Label(
         text='Hello World', font_size=20,
         size_hint=(None, None), size=(200, 75)
      )
      lo.add_widget(self.l1)
      return lo

if __name__ == '__main__':
   AnchorLayoutExample().run()