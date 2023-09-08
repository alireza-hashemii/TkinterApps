from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Image Gallery")
window.iconbitmap("E:\Programming\Tkinter\imgicon\ic3.ico")



image1 = ImageTk.PhotoImage(Image.open(r"imgicon\alireza.png"),name="image1")
image2 = ImageTk.PhotoImage(Image.open(r"imgicon\alireza2.png"),name="image2")
image3 = ImageTk.PhotoImage(Image.open(r"imgicon\alireza3.png"),name="image3")
image4 = ImageTk.PhotoImage(Image.open(r"imgicon\alireza4.png"),name="image4")
image5 = ImageTk.PhotoImage(Image.open(r"imgicon\alireza5.png"),name="image5")

image_list = [image1, image2, image3, image4, image5]


current_image = Label(image=image1)
current_image.grid(row=0, column=0, columnspan=3)

def back():
    pass

def forward(image_number:int):
    global current_image
    global previous_button
    global next_button 

    current_image.grid_forget()
    current_image = Label(image= image_list[image_number - 1])
    next_button = Button(window, text="<<", command=lambda: forward(image_number + 1)).grid(row=1,column=0)
    previous_button = Button(window, text=">>", command=lambda: forward(image_number - 1)).grid(row=1,column=2)



previous_button = Button(window, text="<<", command=back).grid(row=1,column=0)
next_button = Button(window, text=">>L", command=lambda: forward(2)).grid(row=1,column=2)
quit_button = Button(window,text="QUIT", width=10,height=3,bg="red", fg="black", command=window.quit).grid(row=1,column=1)

window.mainloop()
