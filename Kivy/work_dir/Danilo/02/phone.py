from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

class ScrollableGridPopup(Popup):
    def __init__(self, history, **kwargs):
        super().__init__(**kwargs)
        self.grid_layout = GridLayout(cols=1, padding = 20, spacing=20, size_hint=(None, None))
        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))
        
        for entry in history:
            label = Label(text=entry)
            self.grid_layout.add_widget(label)
        scroll_view = ScrollView()
        
        scroll_view.add_widget(self.grid_layout)
        self.content = scroll_view
        

class PhoneApp(App):
    def build(self):
        self.sizes = {"1": 4, "2": 3, "3": 3, "4": 3, "5": 3, "6": 3, "7":4, "8": 3, "9": 4,\
                      "0": 2, "*": 2, "#": 1}
        self.mappings = {"1": ",", "11": ".", "111": "?", "1111": "!",\
                         "2": "a", "22": "b", "222": "c", "3": "d", "33": "e",\
                         "333": "f", "4": "g", "44": "h", "444": "i", "5": "j",\
                         "55": "k", "555": "l", "6": "m", "66": "n", "666": "o",\
                         "7": "p", "77": "q", "777": "r", "7777": "s", "8": "t",\
                         "88": "u", "888": "v", "9": "w", "99": "x", "999": "y", "9999": "z",\
                         "*": "*", "**": "+", "0": "0", "00" : " ", "#": "#"}
        self.prev_key = ""
        root = BoxLayout(orientation="vertical")
        buttons = GridLayout(cols=3, rows=5, spacing=10, padding=10)
        self.b1 = Button(text="1\n(,.?!)", font_size=15)
        self.b2 = Button(text="2\n(abc)", font_size=15)
        self.b3 = Button(text="3\n(def)", font_size=15)
        self.b4 = Button(text="4\n(ghi)", font_size=15)
        self.b5 = Button(text="5\n(jkl)", font_size=15)
        self.b6 = Button(text="6\n(mno)", font_size=15)
        self.b7 = Button(text="7\n(pqrs)", font_size=15)
        self.b8 = Button(text="8\n(tuv)", font_size=15)
        self.b9 = Button(text="9\n(wxyz)", font_size=15)
        self.bstar = Button(text="*+", font_size=15)
        self.b0 = Button(text="0", font_size=15)
        self.bhash = Button(text="#", font_size=15)
        self.send = Button(text="Send")
        self.clear = Button(text="Clear")
        self.history = Button(text="Show History")
        self.output_text = Label(text="")
        self.input = TextInput(hint_text="Your input here", multiline=False, readonly=True, size_hint=(1,None))
        self.timer_running = False

        self.history_list = []
        
        buttons_list = []
        buttons_list.append(self.b1)
        buttons_list.append(self.b2)
        buttons_list.append(self.b3)
        buttons_list.append(self.b4)
        buttons_list.append(self.b5)
        buttons_list.append(self.b6)
        buttons_list.append(self.b7)
        buttons_list.append(self.b8)
        buttons_list.append(self.b9)
        buttons_list.append(self.bstar)
        buttons_list.append(self.b0)
        buttons_list.append(self.bhash)
        for button in buttons_list:
            button.bind(on_press=self.on_button_click)
        self.clear.bind(on_press=self.clear_pressed)
        self.send.bind(on_press=self.send_output)
        self.history.bind(on_press=self.show_history)
        buttons.add_widget(self.b1)
        buttons.add_widget(self.b2)
        buttons.add_widget(self.b3)
        buttons.add_widget(self.b4)
        buttons.add_widget(self.b5)
        buttons.add_widget(self.b6)
        buttons.add_widget(self.b7)
        buttons.add_widget(self.b8)
        buttons.add_widget(self.b9)
        buttons.add_widget(self.bstar)
        buttons.add_widget(self.b0)
        buttons.add_widget(self.bhash)
        buttons.add_widget(self.send)
        buttons.add_widget(self.history)
        buttons.add_widget(self.clear)
        root.add_widget(self.input)
        root.add_widget(buttons)
        root.add_widget(self.output_text)
        return root

    def timer_complete(self, dt):
        if self.prev_key is not "":
            self.input.text += self.mappings[self.prev_key]
        self.prev_key=""
        self.timer_running = False
        
    def on_stop(self):
        Clock.unschedule(self.timer_complete)


    def on_button_click(self, instance):
        char = instance.text[0]
        if self.timer_running: 
            Clock.unschedule(self.timer_complete)
            Clock.schedule_once(self.timer_complete, 1.0) 
        else:
            self.timer_running = True
            Clock.schedule_once(self.timer_complete, 1.0) 
        if(char in self.prev_key and len(self.prev_key) < self.sizes[char]):
            self.prev_key += char
        else:
            if len(self.prev_key) is not 0:
                self.input.text += self.mappings[self.prev_key]
            self.prev_key = char

    def clear_pressed(self, instance):
        self.input.text=""

    def send_output(self, instance):
        self.output_text.text = "Poslata poruka: " + self.input.text
        self.history_list.append(self.input.text)
        self.input.text=""
        
    def show_history(self, instance):
        popup = ScrollableGridPopup(self.history_list, title='History', size_hint=(None, None), size=(400, 400))
        popup.open()


def main():
    PhoneApp().run()

    
if __name__ == "__main__":
    main()
