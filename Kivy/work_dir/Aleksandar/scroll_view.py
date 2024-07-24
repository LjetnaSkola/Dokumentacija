from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button


class ScrollViewApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.input_label = Label(text='Item')
        self.text_input = TextInput(multiline=False, size_hint_y=None, height=40)

        self.input_layout = BoxLayout(orientation='vertical', spacing=10)
        self.input_layout.add_widget(self.input_label)
        self.input_layout.add_widget(self.text_input)
        layout.add_widget(self.input_layout)

        self.scroll_view = ScrollView(size_hint=(1, 1))
        self.stack_layout = StackLayout(size_hint_y=None)
        self.scroll_view.add_widget(self.stack_layout)
        layout.add_widget(self.scroll_view)

        self.submit_button = Button(text='Submit', size_hint_y=None, height=50)
        self.submit_button.bind(on_press=self.add_label)
        layout.add_widget(self.submit_button)

        return layout

    def add_label(self, instance):
        text = self.text_input.text[:5]
        new_label = Label(text=f'Label: {text}', size_hint_y=None, height=40)
        self.stack_layout.add_widget(new_label)
        self.text_input.text = ''


if __name__ == '__main__':
    ScrollViewApp().run()
