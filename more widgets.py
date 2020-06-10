# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:30:13 2020

@author: Wiktoria
"""

from tkinter import Tk, Menu, mainloop


def newfile():
    pass

def openfile():
    pass

def savefile():
    pass

def closefile():
    pass

root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label = 'New', command = newfile)
filemenu.add_command(label = 'Open', command = openfile)
filemenu.add_command(label = 'Save as...', command = savefile)
filemenu.add_command(label = 'Close', command = closefile)
filemenu.add_separator
filemenu.add_command(label = 'Exit', command = root.quit)


menubar.add_cascade(label = 'File', menu = filemenu)

root.config(menu = menubar)



mainloop()

