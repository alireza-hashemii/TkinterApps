from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Image Gallery")
window.iconbitmap("E:\Programming\Tkinter\imgicon\ic3.ico")
# window.geometry("700x400")


image1 = ImageTk.PhotoImage(Image.open(r"imgicon\alireza.png"))
image2 = ImageTk.PhotoImage(Image.open(r"imgicon\alireza2.png"))
image3 = ImageTk.PhotoImage(Image.open(r"imgicon\alireza3.png"))
image4 = ImageTk.PhotoImage(Image.open(r"imgicon\alireza4.png"))
image5 = ImageTk.PhotoImage(Image.open(r"imgicon\alireza5.png"))

image_list = [image1, image2, image3, image4, image5]

mimage = Label(image=image1,width=550,height=470).grid(row=0,column=0,columnspan=3)


next_button = Button(window, text="<<").grid(row=1,column=0)
previous_button = Button(window, text=">>").grid(row=1,column=2)
quit_button = Button(window,text="QUIT", width=10,height=3,bg="red", fg="black", command=window.quit).grid(row=1,column=1)

window.mainloop()
