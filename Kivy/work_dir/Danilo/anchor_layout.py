from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout


class MyApp(App):
    def build(self):
        layout = AnchorLayout(anchor_x="left", anchor_y="bottom")
        
        b1 = Button(text='Button 1', size_hint=(None, None), size=(100, 50))
        b2 = Button(text='Button 2', size_hint=(None, None), size=(100, 50))
        b3 = Button(text='Button 3', size_hint=(None, None), size=(100, 50))
        b4 = Button(text='Button 4', size_hint=(None, None), size=(100, 50))
        b5 = Button(text='Button 5', size_hint=(None, None), size=(100, 50))
        
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
