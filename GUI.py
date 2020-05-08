# -*- coding: utf-8 -*-
"""
Created on Fri May  8 12:24:23 2020

@author: Wiktoria
"""

from tkinter import Tk, Label, Button, mainloop

root = Tk()

count = 0

label = Label(root, text = "Button clicked: " + str(count),
              padx = 30, pady = 30)
label.pack()

def increment():
    global count
    count += 1
    label.configure(text = "Button clicked: " + str(count))
    
button = Button(root, text = "Wow", command = increment)
button.pack()

mainloop()

























