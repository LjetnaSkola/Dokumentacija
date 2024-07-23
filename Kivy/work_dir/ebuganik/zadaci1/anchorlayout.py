import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
class AnchorLayoutApp(App):
    def build(self):
        layout = AnchorLayout(anchor_x ='right', anchor_y ='bottom')
        b1 = Button(size_hint =(.3, .3),background_color =(1.0, 0.0, 0.0, 1.0), text = '1')
        layout.add_widget(b1)
        return layout

if __name__ == '__main__':
    AnchorLayoutApp().run()