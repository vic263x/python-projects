# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:30:13 2020

@author: Wiktoria
"""

from tkinter import Tk, messagebox


root = Tk()

root.withdraw()
messagebox.showinfo('Info', 'You are informed!')

root.deiconify()

root.destroy()
