from tkinter import *

WHITE = "#FFFFFF"
BLUE = "#0D1282"
FONT = "Courier"

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(height=200, width=200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website", bg=WHITE, width=15)
website_label.grid(column=0, row=1)

website_input = Entry(width=36, highlightbackground=WHITE, highlightthickness=2)
website_input.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username", bg=WHITE, pady=10)
email_label.grid(column=0, row=2)

email_input = Entry(width=36, highlightbackground=WHITE, highlightthickness=2)
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password", bg=WHITE, pady=10)
password_label.grid(column=0, row=3)

password_input = Entry(width=21, highlightbackground=WHITE, highlightthickness=2)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", highlightbackground=WHITE)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, highlightbackground=WHITE)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
