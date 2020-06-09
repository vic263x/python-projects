
from tkinter import Tk, Label, Button, mainloop, IntVar

root = Tk()

count = IntVar(root)
count.set(0)

label = Label(root, text="Button clicked: ", padx=30, pady=0)
label.pack()
label = Label(root, textvariable=str(count), 
              padx=30, pady=10)
label.pack()

def increment():
    global count
    count.set(count.get() + 1)

button = Button(root, text="Wow", command=increment)
button.pack()

mainloop()