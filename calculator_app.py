from tkinter import *

# some basic configuration
window = Tk()
window.title("Calculator App")
# window.geometry("240x300")

# Entry
entry = Entry(window, borderwidth=5,width=22)
entry.grid(row=0, column=0, columnspan=4 , padx=10, pady=10)


# functions

def add(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(current) + str(number))

def clear():
    entry.delete(0,END)

def add_button():
    global first_number
    global math_operation 
    math_operation = "addition"
    first_number = entry.get()
    entry.delete(0,END)


def equal_button():
    global second_number
    second_number = entry.get()
    entry.delete(0,END)
    
    if math_operation == "addition":
        entry.insert(0, int(first_number) + int(second_number))
    elif math_operation == "subtraction":
        entry.insert(0, int(first_number) - int(second_number))
    elif math_operation == "division":
        entry.insert(0, int(first_number) / int(second_number))
    elif math_operation == "multiplication":
        entry.insert(0, int(first_number) * int(second_number))


def subtract_button():
    global first_number
    global math_operation 
    math_operation = "subtraction"
    first_number = entry.get()
    entry.delete(0,END)


def divide_button():
    global first_number
    global math_operation 
    math_operation = "division"
    first_number = entry.get()
    entry.delete(0,END)


def multiply_button():
    global first_number
    global math_operation 
    math_operation = "multiplication"
    first_number = entry.get()
    entry.delete(0,END)

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



button_add = Button(window, text="+", padx=18, pady=16, bg="#6ef5ba", command=add_button).grid(row=5, column=0)
button_add = Button(window, text="Clear", padx=36, pady=16, bg="green", command=clear).grid(row=4, column=1, columnspan=2)
button_equal = Button(window, text="=", padx=45, pady=16, bg="#fb36ef", command=equal_button).grid(row=5, column=1, columnspan=2)


button_subtract = Button(window, text="-", padx=19, pady=16, bg="#6ef5ba", command=subtract_button).grid(row=6, column=0)
button_multiply = Button(window, text="x", padx=18, pady=16, bg="#6ef5ba", command=multiply_button).grid(row=6, column=1)
button_divide = Button(window, text="%", padx=18, pady=16, bg="#6ef5ba", command=divide_button).grid(row=6, column=2)


window.mainloop()