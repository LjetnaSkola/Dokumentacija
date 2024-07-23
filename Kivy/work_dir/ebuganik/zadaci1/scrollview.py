import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ScrollLabelApp(App):
    def build(self):
        layout = GridLayout(cols=1, padding=10, spacing=10)
        # Label "Item"
        self.item_label = Label(text='Item',height=40)
        layout.add_widget(self.item_label)
        # Input text
        self.text_input = TextInput(multiline=False, size_hint=(1, None))
        layout.add_widget(self.text_input)
        # Submit button
        self.submit_button = Button(text='Submit', size_hint=(1, None), height=40)
        self.submit_button.bind(on_press=self.on_submit)
        layout.add_widget(self.submit_button)
        # ScrollView
        self.scroll_view = ScrollView(size_hint=(1, None), height=400)
        layout.add_widget(self.scroll_view)
        return layout

    def on_submit(self, instance):
        self.entered_text = self.text_input.text
        # Check if longer than 5 char
        if len(self.entered_text) > 5:
            self.entered_text = self.entered_text[:5]  # in case it is, take first five characters
        # Create new label and add to scroll view
        new_label = Label(text=f'Labela: {self.entered_text}')
        self.scroll_view.add_widget(new_label)


if __name__ == '__main__':
    ScrollLabelApp().run()
