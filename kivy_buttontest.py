import numpy as np
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class myLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(myLayout, self).__init__(**kwargs)

        btn1 = Button(text = "click 1", background_color=[0,0,1,0],pos=(200, 100))
        btn1.bind(on_press=self.clk1)
        btn2 = Button(text = "click 2", pos=(200, 100))
        btn2.bind(on_press=self.clk)
        btn3 = Button(text = "click 3", pos=(50, 100))
        btn3.bind(on_press=self.clk)

        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)

    def clk(self, obj):
        print("Hello WOrld")

    def clk1(self, obj):
        dataset = np.genfromtxt(fname='data.txt',skip_header=1)
        print dataset

class NameApp(App):
    def build(self):
        mL = myLayout()
        return mL

if __name__ == '__main__':
    NameApp().run() 