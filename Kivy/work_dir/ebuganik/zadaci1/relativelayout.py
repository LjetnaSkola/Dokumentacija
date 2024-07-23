import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout

class RelativeLayoutApp(App):
    def build(self):
        Rl = RelativeLayout()
        Rl.add_widget(Button(size_hint =(.2, .2),
                    pos_hint ={'x':0, 'y':0}, text = '1'))
        Rl.add_widget(Button(size_hint =(.2, .2),
                    pos_hint ={'right':1, 'y':0},text = '2'))
        Rl.add_widget(Button(size_hint =(.2, .2),
                    pos_hint ={'center_x':.5, 'center_y':.5},text = '3'))
        Rl.add_widget(Button(size_hint =(.2, .2),
                    pos_hint ={'x':0, 'top':1},text = '4'))
        Rl.add_widget(Button(size_hint =(.2, .2),
                    pos_hint ={'right':1, 'top':1},text = '5'))
        return Rl

if __name__ == '__main__':
    RelativeLayoutApp().run()