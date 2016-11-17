from Tkinter import *
import tkFont
import sys

#the following code is adapted from http://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html
class HomePageGUI:
    def __init__(self, master):
        self.master = master
        master.title("ReFilament PLA recycler") #shows up in the top bar
        master.geometry('800x480') #This seems to be good for the touchscreen, so I'm not gonna mess with it

        master.configure(background = '#d8feff')

        self.header = tkFont.Font(family = 'Roboto', size = 30, weight = 'bold') #This font makes Isaac happy
        self.start_font = tkFont.Font(family = 'Roboto', size = 26, weight = 'bold')
        self.log_font = tkFont.Font(family = 'Roboto', size = 18, weight = 'bold')

        self.label = Label(master, text="So you want to recycle filament...", font = self.header, background = '#d8feff') #prints text above the buttons
        self.label.place(relx = 0.5, rely = 0.2, anchor = N)

        self.start_button = Button(master, text="Let's get started!", font = self.start_font, command=self.start, height = 2, width = 16, background = '#06d109')
        self.start_button.place(relx = 0.5, rely = 0.5, anchor = CENTER) #puts the start button in the center

        self.log_button = Button(master, text="Check the log", font = self.log_font, command=self.log_go, height = 1, width = 12, background = '#06d109')
        self.log_button.place(relx=0.97, rely=0.95, anchor=SE) #log button in bottom right corner

    def start(self):
        print("This will bring you to the next page.")

    def log_go(self):
    	print("This will bring you to the log.")



root = Tk()
my_gui = HomePageGUI(root)
root.mainloop()