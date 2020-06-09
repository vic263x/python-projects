#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:59:32 2020

@author: gaperlinski
"""

from tkinter import Tk, Label, Button, mainloop, NW

#list of colors
cs = ['red','blue','green'] 
#list of fonts
fs = [('times',14,'italic'), ('monaco',24), ('Comic Sans MS',30)]

#current foreground, background, and color
fgval = 0
bgval = 0
fontval = 0

#change the *val variables to next leval value
def switch(x):
  if x < 2: x += 1
  else: x = 0
  return x

#change the font
def fval():
  global fontval
  fontval = switch(fontval)
  label.configure(font=fs[fontval])

#change the foreground
def fgcol():
  global fgval
  fgval = switch(fgval)
  label.configure(fg=cs[fgval])
  
#change the background
def bgcol():
  global bgval
  bgval = switch(bgval)
  label.configure(bg=cs[bgval])
  
#start the GUI
window = Tk()

#make and place a label 
label = Label(window,text='I am a label',
              anchor=NW,
              fg=cs[fgval],bg=cs[bgval],
              font=fs[fontval],padx=30,pady=30)
label.pack()

# button to change foreground 
fg_button = Button(window,text='Foreground',command=fgcol)
fg_button.pack()
   
#button to change background
bg_button = Button(window,text='Background',command=bgcol)
bg_button.pack()

#button to change font 
font_button = Button(window,text='Font',command=fval)
font_button.pack()

quit_button = Button(window,text='Quit',command=quit)
quit_button.pack() 

#go...
mainloop()