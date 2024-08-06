from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors.touchripple import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.actionbar import Button
from kivy.uix.actionbar import BoxLayout
from kivy.app import App


def _five_buttons(layout):
    for i in range(5):
        layout.add_widget(Button(text=f"Button {i}"))


class MyBox(App):
    def build(self):
        self.box = BoxLayout()
        _five_buttons(self.box)
        return self.box


class MyAnchor(App):
    def build(self):
        self.box = AnchorLayout(anchor_x="left", anchor_y="bottom")
        for i in range(5):
            self.box.add_widget(
                Button(text=f"Button {i}", size=(200, 100), size_hint=(None, None))
            )
            self.box.anchor_x = "right"
            self.box.anchor_y = "top"
        return self.box


class MyRelative(App):
    def build(self):
        self.box = RelativeLayout()
        for i in range(5):
            self.box.add_widget(
                Button(
                    text=f"Button {i}",
                    size=(200, 100),
                    size_hint=(None, None),
                    pos_hint=(0.2, 0.2),
                )
            )
        return self.box


class MyGrid(App):
    def build(self):
        self.box = GridLayout(rows=2, cols=3)
        _five_buttons(self.box)
        return self.box


if __name__ == "__main__":
    # MyBox().run()
    # MyGrid().run()
    # MyAnchor().run()
    MyRelative().run()
