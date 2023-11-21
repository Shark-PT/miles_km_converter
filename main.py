from tkinter import *


def button_click():
    pass


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

my_label = Label(text="is equal to", font=("Arial", 20, "bold"))
my_label.grid(column=0, row=1)



my_label = Label(text="Miles", font=("Arial", 16))
my_label.grid(column=2, row=0)

my_label = Label(text="Km", font=("Arial", 16))
my_label.grid(column=2, row=1)

button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)


window.mainloop()
