from tkinter import *
import pandas
import random

FONT = ("Arial", 40, "italic")
FONT_BOLD = ("Arial", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    if current_card:
        words_to_learn.remove(current_card)
        data = pandas.DataFrame(words_to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{current_card['French']}", fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
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
