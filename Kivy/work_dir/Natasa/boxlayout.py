from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyBoxLayoutApp(App):
    def build(self):
        
        layout = BoxLayout(orientation='horizontal')
        buttons = [Button(text=str(i)) for i in range(1, 6)]
        for button in buttons:
            layout.add_widget(button)
        
        return layout

root = MyBoxLayoutApp()
root.run()
