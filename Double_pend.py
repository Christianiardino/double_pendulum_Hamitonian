from GUI_generator import *
from tkinter import *


def button_start_():
    GUI.button_start_pressed()


width_ = 800
height_ = 800

GUI = GUI_generator(width_, height_)
window = GUI.ret_varaibles()

button_start = Button(text="Start", command=lambda: button_start_(), width=43)
button_start.place(x=10, y=height_ - 10)

window.update()
window.mainloop()

