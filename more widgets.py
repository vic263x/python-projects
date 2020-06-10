# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:30:13 2020

@author: Wiktoria
"""

from tkinter import Tk, Entry, StringVar, Button, mainloop

def printit():
    print('Entry:', text.get())

root = Tk()

text = StringVar(root)
text.set('Type something here')


entry = Entry(root, textvariable = text)
entry.bind('<Return>', lambda x: printit())
entry.pack()

button = Button(text = 'Print it!', command = printit)
button.pack()
mainloop()


