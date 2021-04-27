from tkinter import *
import string
from random import sample, choice

def getChars(s):
    chars = string.ascii_lowercase
    if (s['UseNumbers?'] == 1):
        chars += string.digits
    if (s['UseUppercase?'] == 1):
        chars += string.ascii_uppercase
    if (s['UseSpecial?'] == 1):
        chars += "!_#?/"
    return chars

def generatePassword(settings):
    return ''.join([choice(getChars(settings)) for i in range(settings['Length'])])

if __name__ == '__main__':

    settings = {
        'Length': 10,
        'UseNumbers?': 1,
        'UseUppercase?': 1,
        'UseSpecial?': 1,
        }

    root = Tk()
    root.title("Генератор паролей")
    root.geometry("250x250+300+300")

    label_1 = Label(text="Длина пароля")
    label_1.grid(row=0, column=0, sticky=W)

    def onScale(val):
        settings['Length'] = int(val)

    scale = Scale(from_=6, to=30, command=onScale, orient="horizontal")
    scale.grid(row=0, column=1, sticky=W)

    useNumbers = IntVar()
    cbtn_1 = Checkbutton(text="useNumbers", variable=useNumbers, onvalue=1, offvalue=0, padx=15, pady=3)
    cbtn_1.grid(row=1, column=1, sticky=W)

    useUppercase = IntVar()
    cbtn_2 = Checkbutton(text="useUppercase", variable=useUppercase, onvalue=1, offvalue=0, padx=15, pady=3)
    cbtn_2.grid(row=2, column=1, sticky=W)

    useSpecial = IntVar()
    cbtn_3 = Checkbutton(text="useSpecial", variable=useSpecial, onvalue=1, offvalue=0, padx=15, pady=3)
    cbtn_3.grid(row=3, column=1, sticky=W)

    def RefreshSettings():
        settings['Length'] = scale.get()
        settings['UseNumbers?'] = useNumbers.get()
        settings['UseUppercase?'] = useUppercase.get()
        settings['UseSpecial?'] = useSpecial.get()

    def get(event):
        result = StringVar()
        RefreshSettings()

        # вывод пароля
        result.set(generatePassword(settings))
        result_text = Entry(text=result, state='readonly', justify='center', bd=0)
        result_text.grid(row=5, column=1, sticky=W)

    btn = Button(root, text="Get Password", width=10, height=2, bg="white", fg="black")
    btn.grid(row=4, column=1, sticky=W)
    btn.bind("<Button-1>", get)

    root.mainloop()
