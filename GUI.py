from Tkinter import *
import tkFont
import sys

win = Tk()

myFont = tkFont.Font(family = 'Roboto', size = 36, weight = 'bold') #this font makes Isaac happy

def helloPress():
	print("Hey there, lovely human!") #prints to the console. I'm curious about printing to the GUI itself...but that might not be relevant right now

def exitProgram():
	print("Exit button pressed")
	win.quit() #closes the window

win.title("ReFilament PLA recycler") #shows up on the top bar
win.geometry('800x480') #This seems to be good for the touchscreen, so I'm not gonna mess with it

exitButton = Button(win, text = "Exit", font = myFont, command = exitProgram, height = 2, width = 6)
exitButton.pack(side = BOTTOM) #if not attached to a specific side, Exit will appear on top as the first button initialized

helloButton = Button(win, text = "Hiii!", font = myFont, command = helloPress, height = 2, width = 8)
helloButton.pack() #initializes the button at the top b/c it's the first button not attached to a side

mainloop() #Window doesn't open without this