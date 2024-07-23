from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class ButtonExample(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)
        
        # Creating a basic button
        basic_button = Button(text='Click Me!', size_hint=(None, None), size=(200, 50))
        layout.add_widget(basic_button)
        
        # Creating a button with custom background color
        custom_color_button = Button(text='Custom Color', background_color=(0.2, 0.7, 0.3, 1))
        layout.add_widget(custom_color_button)
        
        # Creating a button with an on_press event
        def on_button_press(instance):
            instance.text = 'Clicked!'
        press_button = Button(text='Press Me!')
        press_button.bind(on_press=on_button_press)
        layout.add_widget(press_button)
        
        return layout

if __name__ == '__main__':
    ButtonExample().run()
