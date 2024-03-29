# Import the required libraries
import tkinter as tk
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Changes the name of the window
win.title("Symbol Calculator")

# Set the size of the tkinter window
win.geometry("350x350")

# Define a function to get the length of the current text
def update(event):
   label.config(text="Total Characters: " + str(len(text.get("1.0", 'end-1c'))))

# Create a text widget
text=Text(win, width=50, height=10, font=('Calibri 16'))
text.pack()

# Create a Label widget
label=Label(win, text="", justify=CENTER, font=('12'))
label.pack()

# Bind the buttons with the event
text.bind('<KeyPress>', update)
text.bind('<KeyRelease>', update)

win.mainloop()