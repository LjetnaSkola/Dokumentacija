from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class HelloWorldApp(App):
    def build(self):
        return HelloWorldLayout()

class HelloWorldLayout(BoxLayout):
    def on_button_click(self):
        # This method is called by the KV file
        self.ids.hello_label.text = 'Hello, World!'

if __name__ == '__main__':
    HelloWorldApp().run()
