from tkinter import *

window = Tk()
window.title("Metric Helper")
window.resizable(0,0)

# basic setup
bg_color = "red"
font_family = ('Cambria', 10)
window.config(background=bg_color)

# entry 
input_entry = Entry(window)
output_entry = Entry(window)
input_entry.grid(row=0 ,column=0 , )
output_entry.grid(row=0 ,column=2 , )

# labels 
answer_label = Label(window,text=">>>",font=font_family).grid(row=0, column=1, ipadx=6)


window.mainloop()