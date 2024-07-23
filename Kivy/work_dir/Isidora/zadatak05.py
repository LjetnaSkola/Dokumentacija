from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class AddItemToGridApp(App):
    def build(self):
        self.main_layout = BoxLayout(orientation='vertical', padding=15, spacing=20)

        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=15)
        input_layout.add_widget(Label(text='Item', size_hint_x=None, width=100))
        self.text_input = TextInput(multiline=False, size_hint_x=None, width=250)
        input_layout.add_widget(self.text_input)
        submit_button = Button(text='Submit', size_hint_x=None, width=100)
        submit_button.bind(on_press=self.add_item)
        input_layout.add_widget(submit_button)
        self.main_layout.add_widget(input_layout)

        self.scroll_view = ScrollView(size_hint=(1, 1))
        self.grid_layout = GridLayout(cols=1, size_hint_y=None, spacing=10)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))
        self.scroll_view.add_widget(self.grid_layout)
        self.main_layout.add_widget(self.scroll_view)

        return self.main_layout

    def add_item(self, instance):
        text = self.text_input.text
        if len(text) > 5:
            text = text[:5]
        label = Label(text=f'Label: {text}', size_hint_y=None, height=40)
        self.grid_layout.add_widget(label)
        self.text_input.text = ''


if __name__ == '__main__':
    AddItemToGridApp().run()
