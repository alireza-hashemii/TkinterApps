from tkinter import * 

window = Tk()
opts = [
    "Saturday",
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Friday",
]

clicked = StringVar()
clicked.set(opts[0])
option_menu = OptionMenu(window, clicked, *opts)
option_menu.pack()

window.mainloop()