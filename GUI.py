from Tkinter import *
import tkFont
import sys

win = Tk()

myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')

def helloPress():
	print("Hey there, lovely human!")

def exitProgram():
	print("Exit button pressed")
	win.quit()

win.title("ReFilament PLA recycler") #shows up on the top bar
win.geometry('800x480') #This seems to be good for the touchscreen, so I'm not gonna mess with it

exitButton = Button(win, text = "Exit", font = myFont, command = exitProgram, height = 2, width = 6)
exitButton.pack(side = BOTTOM) #if not attached to a specific side, Exit will appear on top as the first button initialized

helloButton = Button(win, text = "Hiii!", font = myFont, command = helloPress, height = 2, width = 8)
helloButton.pack() #initializes the button at the top b/c it's the first button not attached to a side

mainloop() #Window doesn't open without this