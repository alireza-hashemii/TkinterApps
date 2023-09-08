from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Icon Learning.")
window.iconbitmap("E:\Programming\Tkinter\imgicon\ic2.ico")
window.geometry("700x400")


image = ImageTk.PhotoImage(Image.open(r"imgicon\alireza.png"))
mylabelimg = Label(image=image)
mylabelimg.pack()

quit_button = Button(window,text="QUIT", width=12,height=15,bg="red", fg="black", command=window.quit).pack()

window.mainloop()
