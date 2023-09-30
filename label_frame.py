from tkinter import * 

window = Tk()

labelframe = LabelFrame(window, text="new things are here...", padx=25, pady=5)
button = Button(labelframe, text="Inner Part..", padx=10, pady=7)
labelframe.pack(padx=30, pady=10)
button.pack()
window.mainloop()