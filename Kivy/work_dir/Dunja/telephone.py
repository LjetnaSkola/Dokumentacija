from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import _usleep


class TelephoneApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_key = 123

        self.text_input = TextInput(text="")

        self.num_presses = {  # dictionary za broj pritisaka na svako dugme
            "1": 0, "2": 0, "3": 0,
            "4": 0, "5": 0, "6": 0,
            "7": 0, "8": 0, "9": 0,
            "*": 0, "0": 0, "#": 0
        }
        self.letters = {
            "1": ",.?!",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": "0",
            "#": "#",
            "*": "*+"
        }

    def on_button_press(self, instance):
        key = instance.text[0]

        if self.current_key == 123:
            self.current_key = instance.text
            self.num_presses[key] = (self.num_presses[key] + 1) % len(self.letters[key])

        elif self.current_key == instance.text:
            self.num_presses[key] = (self.num_presses[key] + 1) % len(self.letters[key])

        else:
            key = self.current_key[0]
            letter = self.letters[key][self.num_presses[key]]
            self.num_presses[key] = 0
            self.text_input.text += letter
            self.current_key = instance.text

    def build(self):
        layout = GridLayout(cols=3, padding=20, spacing=10)

        btn_texts = [
            "1 (,.?!)",
            "2 (abc)",
            "3 (def)",
            "4 (ghi)",
            "5 (jkl)",
            "6 (mno)",
            "7 (pqrs)",
            "8 (tuv)",
            "9 (wxyz)",
            "*+",
            "0",
            "#"
        ]

        for text in btn_texts:
            btn = Button(text=text, font_size=20)
            btn.bind(on_press=self.on_button_press)
            layout.add_widget(btn)

        layout.add_widget(self.text_input)
        return layout


if __name__ == "__main__":
    TelephoneApp().run()
