from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock


class MyApp(App):
    def build(self):
        self.layout = GridLayout(rows=5, cols=3)
        self.text_input = TextInput()
        self.press_count_map = {}

        # Mapiranje tipki na odgovarajući tekst
        self.button_map = {
            "1 (,.?!)": ",.?!",
            "2 (abc)": "abc",
            "3 (def)": "def",
            "4 (ghi)": "ghi",
            "5 (jkl)": "jkl",
            "6 (mno)": "mno",
            "7 (pqrs)": "pqrs",
            "8 (tuv)": "tuv",
            "9 (wxyz)": "wxyz",
            "*+": "*+",
            "0": " ",
            "#": "#",
        }

        self.bSend = Button(text="Posalji", background_color=(0, 1, 0, 1))
        self.bDelete = Button(text="Obrisi", background_color=(1, 0, 0, 1))
        self.bDelete.bind(on_press=self.clear)

        self.b1 = Button(text="1 (,.?!)")
        self.b1.bind(on_press=self.on_button_press)
        self.b2 = Button(text="2 (abc)")
        self.b2.bind(on_press=self.on_button_press)
        self.b3 = Button(text="3 (def)")
        self.b3.bind(on_press=self.on_button_press)
        self.b4 = Button(text="4 (ghi)")
        self.b4.bind(on_press=self.on_button_press)
        self.b5 = Button(text="5 (jkl)")
        self.b5.bind(on_press=self.on_button_press)
        self.b6 = Button(text="6 (mno)")
        self.b6.bind(on_press=self.on_button_press)
        self.b7 = Button(text="7 (pqrs)")
        self.b7.bind(on_press=self.on_button_press)
        self.b8 = Button(text="8 (tuv)")
        self.b8.bind(on_press=self.on_button_press)
        self.b9 = Button(text="9 (wxyz)")
        self.b9.bind(on_press=self.on_button_press)
        self.b10 = Button(text="*+")
        self.b10.bind(on_press=self.on_button_press)
        self.b11 = Button(text="0")
        self.b11.bind(on_press=self.on_button_press)
        self.b12 = Button(text="#")
        self.b12.bind(on_press=self.on_button_press)

        self.layout.add_widget(self.bDelete)
        self.layout.add_widget(self.text_input)
        self.layout.add_widget(self.bSend)
        self.layout.add_widget(self.b1)
        self.layout.add_widget(self.b2)
        self.layout.add_widget(self.b3)
        self.layout.add_widget(self.b4)
        self.layout.add_widget(self.b5)
        self.layout.add_widget(self.b6)
        self.layout.add_widget(self.b7)
        self.layout.add_widget(self.b8)
        self.layout.add_widget(self.b9)
        self.layout.add_widget(self.b10)
        self.layout.add_widget(self.b11)
        self.layout.add_widget(self.b12)
        self.current_button = None
        self.current_press_count = 0
        self.repeat_interval = 0.2  # Interval za ponavljanje pritiska (u sekundama)
        self.clock_event = None

        return self.layout

    def on_button_press(self, instance):
        # Prekidamo prethodni događaj sata ako postoji
        if self.clock_event:
            self.clock_event.cancel()

        button_text = instance.text

        # Ako tipka već postoji u mapi broja pritisaka, ažuriramo broj pritisaka za tu tipku
        if button_text in self.press_count_map:
            self.press_count_map[button_text] += 1
        else:
            self.press_count_map[button_text] = 1

        # Dobivamo trenutni broj pritisaka za tu tipku
        self.current_button = button_text
        self.current_press_count = self.press_count_map[button_text]

        # Pokrećemo sat kako bismo pratili brzinu pritiska
        self.clock_event = Clock.schedule_once(
            self.update_text_input, self.repeat_interval
        )

    def on_button_release(self, instance):
        # Prekidamo prethodni događaj sata ako postoji
        if self.clock_event:
            self.clock_event.cancel()

    def update_text_input(self, dt):
        # Dobivamo odgovarajući tekst za trenutni broj pritisaka
        if self.current_button in self.button_map:
            characters = self.button_map[self.current_button]
            index = (self.current_press_count - 1) % len(
                characters
            )  # Modulo operacija za cikličko pretraživanje znakova
            character = characters[index]
            self.text_input.text += character

        # Resetiramo brojače i varijable
        self.current_button = None
        self.current_press_count = 0
        self.press_count_map.clear()

    def clear_input(self):
        self.text_input.text = ""
        if self.clock_event:
            self.clock_event.cancel()

    # def on_button_press(self, instance):
    #     button_text = instance.text
    #
    #     # Ako tipka već postoji u mapi broja pritisaka, ažuriramo broj pritisaka za tu tipku
    #     if button_text in self.press_count_map:
    #         self.press_count_map[button_text] += 1
    #     else:
    #         self.press_count_map[button_text] = 1
    #
    #     # Dobivamo trenutni broj pritisaka za tu tipku
    #     press_count = self.press_count_map[button_text]
    #
    #     # Dobivamo odgovarajući tekst za trenutni broj pritisaka
    #     if button_text in self.button_map:
    #         characters = self.button_map[button_text]
    #         index = (press_count - 1) % len(
    #             characters
    #         )  # Modulo operacija za cikličko pretraživanje znakova
    #         character = characters[index]
    #         self.text_input.text += character
    #
    # def clear_input(self):
    #     self.text_input.text = ""
    #     self.press_count_map.clear()
    #
    def clear(self, instance):
        self.text_input.text = ""
        self.press_count_map.clear()


if __name__ == "__main__":
    MyApp().run()
