from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image


window = Tk()

# def for choosing a file in between
def selection():
    global lbl
    global filename
    filename = window.filename = filedialog.askopenfilename(initialdir="Pictures/Camera Roll",
                        title="select a file",filetypes=(("png files","*.png"),("all filess",("*"))))

    sub_window = Toplevel()
    lbl = Label(sub_window, image=filename).pack()




button_ = Button(window, text="wanna choose a Photo?", bg="#bfeb3e" , padx=30, pady=26, command=selection).pack()

window.mainloop()