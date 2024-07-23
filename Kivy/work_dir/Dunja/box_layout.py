from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutApp(App):
    def build(self):
        # Create a BoxLayout with vertical orientation
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Create five buttons and add them to the layout
        for i in range(5):
            button = Button(text=f"Button {i + 1}")
            layout.add_widget(button)

        return layout


if __name__ == "__main__":
    BoxLayoutApp().run()
