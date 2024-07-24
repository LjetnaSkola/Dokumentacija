from renderer import Renderer
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Rotate
    
class MyApp(App):
    count = 0
    mappings = {0: (1,1,0,0), 1: (1,-1,0,0), 2: (1,0,1,0), 3: (1,0,-1,0), 4: (1,0,0,1), 5: (1,0,0,-1)}
    def build(self):
        self.layout = RelativeLayout()
        self.button = Button(text="Change direction", size_hint=(None,None))
        self.renderer = Renderer(1,1,0,0)
        self.button.bind(on_press=self.on_click)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.renderer)
        return self.layout
        

    def on_click(self, instance):
        if MyApp.count >= 6:
            MyApp.count = 0
        count = MyApp.count
        self.layout.remove_widget(self.layout.children[0])
        self.renderer = Renderer(MyApp.mappings[count][0], MyApp.mappings[count][1], MyApp.mappings[count][2],MyApp.mappings[count][3])
        self.layout.add_widget(self.renderer)
        print(f"{MyApp.mappings[count][0]} {MyApp.mappings[count][1]} {MyApp.mappings[count][2]} {MyApp.mappings[count][3]}")
        MyApp.count+=1
    

def main():
    MyApp().run()

if __name__ == "__main__":
    main()
