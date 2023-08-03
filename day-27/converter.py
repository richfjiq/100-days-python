from tkinter import *

FONT = ("Arial", 24)

window = Tk()
window.title("Mile to km Converter")
window.minsize(width=340, height=150)
window.config(padx=20, pady=20)


def convert_miles():
    km = round(float(miles_input.get()) * 1.6, 2)
    result_label.config(text=f"{km}")


miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)

result_label = Label(text="0", font=FONT)
result_label.grid(column=1, row=1)

km_label = Label(text="km", font=FONT)
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=convert_miles)
button.grid(column=1, row=2)

window.mainloop()
