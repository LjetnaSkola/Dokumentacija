from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class TextInputExample(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)
        
        # Single-line TextInput
        single_line_input = TextInput(hint_text='Enter your name', multiline=False)
        layout.add_widget(single_line_input)
        
        # Multi-line TextInput
        multi_line_input = TextInput(hint_text='Enter your message', multiline=True)
        layout.add_widget(multi_line_input)
        
        # Password TextInput
        password_input = TextInput(hint_text='Enter password', password=True)
        layout.add_widget(password_input)
        
        return layout

if __name__ == '__main__':
    TextInputExample().run()
