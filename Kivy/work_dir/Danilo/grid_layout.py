from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2, rows=4)
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
