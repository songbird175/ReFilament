from Tkinter import *
import tkFont
import sys

#the following code is adapted from http://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("ReFilament PLA recycler") #shows up in the top bar
        master.geometry('800x480') #This seems to be good for the touchscreen, so I'm not gonna mess with it

        self.font = tkFont.Font(family = 'Roboto', size = 36, weight = 'bold') #This font makes Isaac happy

        self.label = Label(master, text="This is our first GUI!", font = self.font) #sweet, this prints text above the buttons
        self.label.pack()

        self.greet_button = Button(master, text="Hiii!", font = self.font, command=self.greet, height = 2, width = 8)
        self.greet_button.pack()

        self.close_button = Button(master, text="Exit", font = self.font, command=master.quit, height = 2, width = 6)
        self.close_button.pack(side = BOTTOM)

    def greet(self):
        print("Hey there, lovely human!")



root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()