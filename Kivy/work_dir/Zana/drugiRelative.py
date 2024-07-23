from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = RelativeLayout()
        button_width = 100
        button_height = 100
        spacing = 10
        num_buttons = 5

        container_width = num_buttons * button_width + (num_buttons - 1) * spacing

        layout.size_hint = (None, None)
        layout.size = (container_width, button_height)

        x_pos = 0

        for i in range(1, num_buttons + 1):
            button = Button(text=f'Button {i}', size_hint=(None, None), size=(button_width, button_height))
            button.pos = (x_pos, 0)
            layout.add_widget(button)

            x_pos += button_width + spacing

        return layout

if __name__ == '__main__':
    MyApp().run()
