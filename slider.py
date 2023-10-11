from tkinter import *


window = Tk()
window.geometry("300x350")

def slide():
    my_label = Label(window, text= vertical_slider.get()).pack()
    window.geometry("{!s}x{!s}".format(horizontal_slider.get(),(vertical_slider.get())))


vertical_slider = Scale(window, from_=0, to=600, width=90)
vertical_slider.pack(anchor=N)

horizontal_slider = Scale(window, from_=0, to=500, orient=HORIZONTAL)
horizontal_slider.pack()

button = Button(window, text="Change Scale", command=slide,border=3,background="blue")
button.pack()

window.mainloop()