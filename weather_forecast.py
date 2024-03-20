from tkinter import messagebox, ttk
from tkinter import *
from tkinter import Tk
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


root.mainloop()







