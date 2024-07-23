from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyGridLayoutApp(App):
    def build(self):
    
        layout = GridLayout(cols=2)

        for i in range(1, 6):
            button = Button(text=str(i))
            layout.add_widget(button)

        return layout

if __name__ == '__main__':
    MyGridLayoutApp().run()
