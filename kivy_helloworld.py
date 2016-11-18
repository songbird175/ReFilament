import numpy as np
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class myLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(myLayout, self).__init__(**kwargs)

        label1 = Label(text="WELL", background_color=[0,0,1,1])
        btn1 = Button(text = "click 1", background_color=[0,0,1,1])
        btn1.bind(on_press=self.clk)

        self.add_widget(label1)
        self.add_widget(btn1)

    def clk(self, obj):
        print("Hello World")

class TestApp(App):
    def build(self):
    	mL = myLayout()
        return mL

if __name__ == "__main__":	
	TestApp().run()