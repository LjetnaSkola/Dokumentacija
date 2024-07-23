from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyScrollViewApp(App):
    def build(self):
    
        main_layout = GridLayout(cols=1, spacing=10, padding=10)

        input_layout = GridLayout(cols=2, spacing=10)
        input_layout.add_widget(Label(text='Item'))
        self.text_input = TextInput(multiline=False)
        input_layout.add_widget(self.text_input)
        main_layout.add_widget(input_layout)

        submit_button = Button(text='Submit', on_press=self.submit_text)
        main_layout.add_widget(submit_button)

        self.scroll_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.scroll_layout.bind(minimum_height=self.scroll_layout.setter('height'))
        
        scroll_view = ScrollView()
        scroll_view.add_widget(self.scroll_layout)
        main_layout.add_widget(scroll_view)

        return main_layout

    def submit_text(self, instance):

        uneseni_tekst = self.text_input.text[:5]

        nova_labela = Label(text=f'Labela: {uneseni_tekst}')

        self.scroll_layout.add_widget(nova_labela)

if __name__ == '__main__':
    MyScrollViewApp().run()
