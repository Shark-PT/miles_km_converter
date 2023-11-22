from tkinter import *


def button_click():
    miles = float(input_miles.get())
    km = round(miles * 1.6)
    result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

input_miles = Entry(width=7)
input_miles.insert(END, string="0")
input_miles.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 16))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Arial", 16))
is_equal_label.grid(column=0, row=1)

result_label = Label(text="0", font=("Arial", 16))
result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km", font=("Arial", 16))
kilometer_label.grid(column=2, row=1)

button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)


window.mainloop()
