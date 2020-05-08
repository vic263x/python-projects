# -*- coding: utf-8 -*-
"""
Created on Fri May  8 12:24:23 2020

@author: Wiktoria
"""

from tkinter import Tk, Button, Label, filedialog, mainloop 

root = Tk()

file_label = Label(root, text = "File location...")
file_label.pack()

def get_file():
    file_path = filedialog.askopenfilename()
    file_label.configure(text = file_path)

file_button = Button(root, text = "get file location", command = get_file)
file_button.pack()

quit_button = Button(root, text = "Quit", command = quit)
quit_button.pack()

mainloop()

























