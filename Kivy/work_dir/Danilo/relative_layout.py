from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout


class MyApp(App):
    def build(self):
        layout = RelativeLayout()
        
        b1 = Button(text='Button 1', size_hint=(None, None), size=(100, 50))
        b2 = Button(text='Button 2', size_hint=(None, None), size=(100, 50))
        b3 = Button(text='Button 3', size_hint=(None, None), size=(100, 50))
        b4 = Button(text='Button 4', size_hint=(None, None), size=(100, 50))
        b5 = Button(text='Button 5', size_hint=(None, None), size=(100, 50))
        
        b1.pos_hint = {'x': 0.1, 'y': 0.5}
        b2.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        b3.pos_hint = {'right': 0.9, 'y': 0.5}
        b4.pos_hint = {'x': 0.5, 'top': 0.9}
        b5.pos_hint = {'x': 0.5, 'y': 0.1}
        
        layout.add_widget(b1)
        layout.add_widget(b2)
        layout.add_widget(b3)
        layout.add_widget(b4)
        layout.add_widget(b5)
        
        return layout
        
def main():
    MyApp().run()

if __name__ == "__main__":
    main()
