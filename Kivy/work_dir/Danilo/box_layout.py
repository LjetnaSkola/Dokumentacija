from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        b1 = Button(text='Button 1')
        b2 = Button(text='Button 2')
        b3 = Button(text='Button 3')
        b4 = Button(text='Button 3')
        b5 = Button(text='Button 5')
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
