from Tkinter import *
import tkFont
import sys

win = Tk()

myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')

def helloPress():
	sys.stdout = TextRedirector("Hey there, lovely human!")

def exitProgram():
	print("Exit button pressed")
	win.quit()

win.title("First GUI")
win.geometry('800x480')

exitButton = Button(win, text = "Exit", font = myFont, command = exitProgram, height = 2, width = 6)
exitButton.pack(side = BOTTOM)

helloButton = Button(win, text = "Hiii!", font = myFont, command = helloPress, height = 2, width = 8)
helloButton.pack()

mainloop()