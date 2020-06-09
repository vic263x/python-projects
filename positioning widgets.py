# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 17:10:21 2020

@author: Wiktoria
"""

from tkinter import Tk, Label, mainloop, NONE, X, Y, BOTH, TOP, LEFT, RIGHT, BOTTOM

root = Tk()

label = Label(root, text = 'Position me!', bg = 'pink')

label.pack(side =RIGHT, ipadx=30, ipady=20)

mainloop()
