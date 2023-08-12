from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Arial", 24)


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

language_label = Label(text="French", font=("Arial", 40, "italic"), bg="white")
language_label.place(x=400, y=150, anchor="center")
word_label = Label(text="trouve", font=("Arial", 40, "italic"), bg="white")
word_label.place(x=400, y=263, anchor="center")

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(
    image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR
)
wrong_button.grid(column=0, row=1)
right_image = PhotoImage(file="images/right.png")
right_button = Button(
    image=right_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR
)
right_button.grid(column=1, row=1)

window.mainloop()
