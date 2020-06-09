# -*- coding: utf-8 -*-
"""
Created on Fri May  8 13:23:10 2020

@author: Wiktoria
"""

from tkinter import Tk, Label, Button, mainloop, filedialog, IntVar

count = 0
root = Tk()
file_path = IntVar(root)
file_path.set("Button clicked: " + str(count))



file_label = Label(root, textvariable = file_path, 
              padx=30, pady=30)
file_label.pack()



def get_file():
    #global count
   
    file_path.set(filedialog.countdown())
    #count += 1
    
file_button = Button(root, text = "Wow", command = get_file)
file_button.pack()
    


mainloop()