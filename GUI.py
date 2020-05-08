# -*- coding: utf-8 -*-
"""
Created on Fri May  8 12:24:23 2020

@author: Wiktoria
"""

from tkinter import Tk, Frame, Button, LEFT, mainloop


#start a tkinter window app

root = Tk()

#make a frame widget 

frame = Frame(root)
frame.pack() #positioning the element on the screen


# make a button

button = Button(frame, padx = 20, pady = 10,
                text = 'quit', command = quit)

button.pack(side = LEFT, padx = 5, pady = 3)

#wait for something to happen

mainloop()



























