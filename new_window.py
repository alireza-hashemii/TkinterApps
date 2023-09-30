from tkinter import *


window = Tk()
window.title("A creative title")


def want_window():
    sub_window = Toplevel()
    sub_window.geometry("700x300")
    button = Button(sub_window, text="Close",padx=6,pady=5,command=sub_window.destroy).pack()

button = Button(window, text="Are ya lookin' for another window?",bg="green",
            padx=30, pady=25, border=7, command=want_window).pack()



window.mainloop()