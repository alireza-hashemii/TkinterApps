from tkinter import *

# some basic configuration
window = Tk()
window.title("Calculator App")
# window.geometry("240x300")

# Entry
entry = Entry(window, borderwidth=5,width=22)
entry.grid(row=0, column=0, columnspan=4 , padx=10, pady=10)

# add function
def add(number):
    entry.delete(0,END)
    entry.insert(0,number)


# keys of calculator are here
button1 = Button(window, text="1", padx=18, pady=16 , command=lambda: add(1), bg="#71f6f6").grid(row=1, column=0)
button2 = Button(window, text="2", padx=18, pady=16, command=lambda: add(2), bg="#71f6f6").grid(row=1, column=1)
button3 = Button(window, text="3", padx=18, pady=16, command=lambda: add(3), bg="#71f6f6").grid(row=1, column=2)

button4 = Button(window, text="4", padx=18, pady=16, command=lambda: add(4), bg="#71f6f6").grid(row=2, column=0)
button5 = Button(window, text="5", padx=18, pady=16, command=lambda: add(5), bg="#71f6f6").grid(row=2, column=1)
button6 = Button(window, text="6", padx=18, pady=16, command=lambda: add(6), bg="#71f6f6").grid(row=2, column=2)

button7 = Button(window, text="7", padx=18, pady=16, command=lambda: add(7), bg="#71f6f6").grid(row=3, column=0)
button8 = Button(window, text="8", padx=18, pady=16, command=lambda: add(8), bg="#71f6f6").grid(row=3, column=1)
button9 = Button(window, text="9", padx=18, pady=16, command=lambda: add(9), bg="#71f6f6").grid(row=3, column=2)
button9 = Button(window, text="0", padx=18, pady=16, command=lambda: add(0), bg="#71f6f6").grid(row=4, column=0)



button_add = Button(window, text="+", padx=18, pady=16, bg="#6ef5ba").grid(row=5, column=0)
button_add = Button(window, text="Clear", padx=36, pady=16, bg="green").grid(row=4, column=1, columnspan=2)
button_equal = Button(window, text="=", padx=45, pady=16, bg="#fb36ef").grid(row=5, column=1, columnspan=2)


window.mainloop()