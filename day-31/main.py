from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Arial", 40, "italic")
FONT_BOLD = ("Arial", 60, "bold")

# ---------------------------------------- Pick random word ----------------------------------------
data = pandas.read_csv("data/french_words.csv")
words_dict = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(words_dict)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=f"{current_card['French']}")


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")

canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=FONT)
card_word = canvas.create_text(400, 263, text="word", font=FONT_BOLD)
canvas.grid(column=0, row=0, columnspan=2)


wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(
    image=wrong_image,
    highlightthickness=0,
    highlightbackground=BACKGROUND_COLOR,
    command=next_card,
)
wrong_button.grid(column=0, row=1)
right_image = PhotoImage(file="images/right.png")
right_button = Button(
    image=right_image,
    highlightthickness=0,
    highlightbackground=BACKGROUND_COLOR,
    command=next_card,
)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
