from tkinter import *
from tkinter import messagebox

WHITE = "#FFFFFF"
BLUE = "#0D1282"
FONT = "Courier"

# ---------------------------------------- PASSWORD GENERATOR ----------------------------------------


# ---------------------------------------- SAVE PASSWORD ----------------------------------------
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty."
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?",
        )

        if is_ok:
            # Best approach
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, "end")
                password_input.delete(0, "end")
            # f = open("data.txt", "a")
            # f.write(f"{website} | {email} | {password}\n")
            # f.close()


# ---------------------------------------- UI SETUP ----------------------------------------

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(height=200, width=200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website", bg=WHITE, width=15)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username", bg=WHITE, pady=10)
email_label.grid(column=0, row=2)
password_label = Label(text="Password", bg=WHITE, pady=10)
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=36)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_input = Entry(width=36)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "rfjiq1986@gmail.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", highlightbackground=WHITE)
generate_button.grid(column=2, row=3)
add_button = Button(
    text="Add", width=36, highlightbackground=WHITE, command=save_password
)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
