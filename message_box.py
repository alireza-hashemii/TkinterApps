from tkinter import *
from tkinter import messagebox

window = Tk()

# Cancel returs 0 and retry and ok button return 1 as a response.

def popup():
    response = messagebox.askretrycancel("An Error Occured.", "Let's Fix This Brother")
    # label = Label(window, text=response).pack()
    if response == 1:
        label = Label(window, text="You clicked retry Alright").pack()
        popup()
    elif response == 0:
        label = Label(window, text="You clicked no alright Bye").pack()

button = Button(window, bg="red", text="Let's see what happens.",command=popup).pack()
window.mainloop()

