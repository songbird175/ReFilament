from Tkinter import *
import tkFont
import sys

#the following code is adapted from http://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("ReFilament PLA recycler") #shows up in the top bar
        master.geometry('800x480') #This seems to be good for the touchscreen, so I'm not gonna mess with it

        self.font = tkFont.Font(family = 'Roboto', size = 24, weight = 'bold') #This font makes Isaac happy

        self.label = Label(master, text="This is our first GUI!", font = self.font) #sweet, this prints text above the buttons
        self.label.pack()

        self.greet_button = Button(master, text="Hiii!", font = self.font, command=self.greet, height = 2, width = 8)
        self.greet_button.place(relx = 0.5, rely = 0.5, anchor = CENTER) #puts the greet button in the center (taken from http://stackoverflow.com/questions/18736465/how-to-center-tkinter-wiget)

        self.close_button = Button(master, text="Exit", font = self.font, command=master.quit, height = 2, width = 6)
        self.close_button.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE) #exit button in bottom right corner (taken from http://stackoverflow.com/questions/25396197/tkinter-put-a-widget-in-the-lower-right-corner-using-place)

    def greet(self):
        print("Hey there, lovely human!")



root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()