from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class ReferencingApp(App):
    click_count = 0

    def build(self):
        layout = BoxLayout(orientation='vertical')
        return layout
    
    def react_on_press(self, instance):
        instance.text = 'pressed'


if __name__ == '__main__':
    ReferencingApp().run()
