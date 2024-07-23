from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MyApp(App):
    def build(self):
        layout = AnchorLayout(anchor_x='left', anchor_y='bottom')
        button_width = 100
        spacing = 10
        num_buttons = 5

        container_width = num_buttons * button_width + (num_buttons - 1) * spacing

        for i in range(1, num_buttons + 1):
            button = Button(text=f'Button {i}', size_hint=(None, None), size=(100, 100))
            layout.add_widget(button)

        return layout

if __name__ == '__main__':
    MyApp().run()
