# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:30:13 2020

@author: Wiktoria
"""

from tkinter import Tk, mainloop, Listbox, Button, END, MULTIPLE

def getitem():
    print('Element(s) selected: ', mylist.curselection())

root = Tk()

mylist = Listbox(root, selectmode = MULTIPLE)

for line in range(5):
    mylist.insert(END, 'This is line number ' + str(line))
mylist.pack()

button = Button(text = 'Confirm', command = getitem)
button.pack()


mainloop()
