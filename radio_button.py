from tkinter import *

window = Tk()

opt = IntVar()
opt.set(2)

def clicked(val):
    global mylabel
    mylabel = Label(window, text=val).pack()

Radiobutton(window, text="Option-1", variable=opt,
            value=1, command=lambda: clicked(1)).pack()
Radiobutton(window, text="Option-2", variable=opt,
            value=2, command=lambda: clicked(2)).pack()


mylabel = Label(window, text=opt.get()).pack()
window.mainloop()