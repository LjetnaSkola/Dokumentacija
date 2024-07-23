from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=5, spacing=10)

        for i in range(1, 6):
            button = Button(text=f'Button {i}', size_hint=(None, None), size=(100, 100))
            layout.add_widget(button)

        return layout

if __name__ == '__main__':
    MyApp().run()
