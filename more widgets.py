# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:30:13 2020

@author: Wiktoria
"""

from tkinter import Tk, mainloop, Listbox, Button, END, MULTIPLE, Scrollbar, RIGHT, Y, LEFT, BOTH, BOTTOM

def getitem():
    print('Element(s) selected: ', mylist.curselection())

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

mylist = Listbox(root, selectmode = MULTIPLE, yscrollcommand = scrollbar.set)

scrollbar.config(command = mylist.yview)

for line in range(100):
    mylist.insert(END, 'This is line number ' + str(line))
mylist.pack(side = LEFT, fill = BOTH)



button = Button(text = 'Confirm', command = getitem)
button.pack(side = BOTTOM)


mainloop()
