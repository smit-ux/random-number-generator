from tkinter import *

rand = Tk()

rand.geometry("300x300")
rand.title("GENERATE RANDOM NUMBER")
rand.grid()
rand.config(bg='black')
rand.frame()

def randnum(event):
	import random
	value =random.randint(1,32678)
	print(value)
	updateDisplay(value)


def updateDisplay(myString):
	displayVariable.set(myString)


import tkinter.font as font
myFont = font.Font(family='Courier', size=15, weight='bold')
button_1 = Button(rand, text="GENERATE" , bg='#ffffff', activebackground='#00ff00')
button_1['font'] = myFont
button_1.bind("<Button-1>", randnum)
button_1.pack()
displayVariable = StringVar()
displayLabel = Label(rand, textvariable=displayVariable)
displayLabel.pack()
rand.mainloop()