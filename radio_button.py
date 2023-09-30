from tkinter import *

window = Tk()

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Onion", "Onion"),
    ("Margarita", "Margarita"),
]

opt = StringVar()
opt.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(window, text=text, variable=opt, value=mode).pack()


# opt = IntVar()
# opt.set(2)

def clicked(val):
    global mylabel
    mylabel = Label(window, text=val).pack()

# Radiobutton(window, text="Option-1", variable=opt,
#             value=1, command=lambda: clicked(1)).pack()
# Radiobutton(window, text="Option-2", variable=opt,
#             value=2, command=lambda: clicked(2)).pack()

choosable_button = Button(window, text="Wanna know the mode?",
                    padx=15, pady=12,command=lambda: clicked(opt.get())).pack()
# mylabel = Label(window, text=opt.get()).pack()
window.mainloop()