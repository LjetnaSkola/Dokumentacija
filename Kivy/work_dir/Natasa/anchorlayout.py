from kivy.app import App  
from kivy.uix.anchorlayout import AnchorLayout  
from kivy.uix.boxlayout import BoxLayout  
from kivy.uix.button import Button 
 
class AnchorLayoutApp(App): 
	
	def build(self): 
		layout = AnchorLayout(anchor_x ='right', anchor_y ='bottom')
		btn = Button(text ='Button 1', size_hint =(.3, .3))
	
		layout.add_widget(btn) 
		return layout 
        
root = AnchorLayoutApp() 
root.run() 
