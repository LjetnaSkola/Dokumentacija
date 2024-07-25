from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from renderer import Renderer


class MainApp(App):
    def build(self):
        layout = RelativeLayout()

        # Create an instance of Renderer
        self.renderer = Renderer()
        self.renderer.size = layout.size
        self.renderer.pos = (0, 0)
        layout.add_widget(self.renderer)

        # Create buttons for axis selection
        self.axis_buttons = {
            'X': Button(text="Rotate X", size_hint=(None, None), size=(200, 50), pos=(10, 130)),
            'Y': Button(text="Rotate Y", size_hint=(None, None), size=(200, 50), pos=(220, 130)),
            'Z': Button(text="Rotate Z", size_hint=(None, None), size=(200, 50), pos=(430, 130))
        }

        # Bind buttons to axis selection functions
        for axis, button in self.axis_buttons.items():
            button.bind(on_press=self.toggle_axis)
            layout.add_widget(button)

        # Create buttons for toggling rotation direction
        self.direction_buttons = {
            'X': Button(text="Toggle X Rotation", size_hint=(None, None), size=(200, 50), pos=(10, 70), opacity=0),
            'Y': Button(text="Toggle Y Rotation", size_hint=(None, None), size=(200, 50), pos=(220, 70), opacity=0),
            'Z': Button(text="Toggle Z Rotation", size_hint=(None, None), size=(200, 50), pos=(430, 70), opacity=0)
        }

        # Bind direction buttons to change rotation direction functions
        for axis, button in self.direction_buttons.items():
            button.bind(on_press=self.change_rotation_direction)
            layout.add_widget(button)

        # Create reset button
        self.reset_button = Button(
            text="Reset Rotation",
            size_hint=(None, None),
            size=(200, 50),
            pos=(10, 10)
        )
        self.reset_button.bind(on_press=self.reset_rotation)
        layout.add_widget(self.reset_button)

        # Set to keep track of active axes
        self.active_axes = set()

        return layout

    def toggle_axis(self, instance):
        axis = instance.text.split(" ")[-1]  # Get the axis (X, Y, Z)
        if axis in self.active_axes:
            self.active_axes.remove(axis)
            self.renderer.set_rotation_axis(axis, False)  # Disable rotation for this axis
            self.direction_buttons[axis].opacity = 0
        else:
            self.active_axes.add(axis)
            self.renderer.set_rotation_axis(axis, True)  # Enable rotation for this axis
            self.direction_buttons[axis].opacity = 1

    def change_rotation_direction(self, instance):
        axis = instance.text.split(" ")[-2]  # Get the axis (X, Y, Z)
        self.renderer.change_rotation_direction(axis)

    def reset_rotation(self, instance):
        self.renderer.reset_rotation()  # Call the reset method in Renderer


if __name__ == "__main__":
    MainApp().run()
