from tkinter import *

window = Tk()
window.resizable(0,0)
window.title("Marsh Translator")
window.geometry("800x500")
window.config(bg="#16ff72")


morse = {
        # Letters
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        # Numbers
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        # Punctuation
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
}

def morse_handler():
    pass




info_label  = Label(window, text="Enter your text here", bg="#16ff72").pack()
info_entry  = Entry(
            window,
            bd=2,
            relief="groove",
            font=("Arial", 15)
            )
info_entry.pack(fill="x", padx=50, pady=30,ipady=20)

generate_morse_from_str_btn = Button(window, text="From string to morse",padx=35,pady=10, command=morse_handler).pack(ipady=5)
generate_str_from_morse = Button(window, text="From Morse to string", padx=34, pady=10).pack(ipady=6)


output_label = Label(window, font=("Arial", 25)).pack(fill="x",padx=40,pady=30)

morse_source_btn = Button(window, text="Morse Codes").pack()

window.mainloop()