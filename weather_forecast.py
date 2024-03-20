from tkinter import messagebox, ttk
from tkinter import *
from tkinter import Tk
from tkinter import Label
from timezonefinder import TimezoneFinder
from datetime import datetime
from geopy.geocoders import Nominatim
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(0,0)

# search box
search_image = PhotoImage(file="imgicon/search.png")
myimage = Label(image=search_image)

myimage.place(x=20, y=20)
textfield = Entry(
            root,
            justify="center",
            width=17,
            font=("poppins", 25, 'bold'),
            bg="#404040",
            fg="white",
            border=0
        )
textfield.place(x=50,y=40)
textfield.focus()

search_icon = PhotoImage(file="imgicon/search_icon.png")
my_image_icon = Button(
            image=search_icon, 
            borderwidth=0, 
            cursor="hand2",
            bg="#404040"
        )
my_image_icon.place(x=400, y=34)


# Logo
Logo_image = PhotoImage(file="imgicon/logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

# Bottom box
Frame_image = PhotoImage(file="imgicon/box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5 , pady=5,side=BOTTOM )


# Label

label1=Label(root, text="WIND", font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label1.place(x=120, y=400)

label2=Label(root, text="HUMIDITY", font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label2.place(x=250, y=400)

label3=Label(root, text="DESCRIPTION", font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label3.place(x=430, y=400)

label4=Label(root, text="PRESSURE", font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label4.place(x=650, y=400)


t = Label(font=('arial', 70, 'bold'), fg="#ee666d")
t.place(x=400, y=150)

c = Label(font=('arial', 15, 'bold'))
c.place(x=400, y=250)

w = Label(text="...", font=('arial',20, 'bold'),bg="#1ab5ef")
w.place(x=120, y=430)

h = Label(text="...", font=('arial',20, 'bold'),bg="#1ab5ef")
h.place(x=280, y=430)

d = Label(text="...", font=('arial',20, 'bold'),bg="#1ab5ef")
d.place(x=450, y=430)

p = Label(text="...", font=('arial',20, 'bold'),bg="#1ab5ef")
p.place(x=670, y=430) 



root.mainloop()










