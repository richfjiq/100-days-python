from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

WHITE = "#FFFFFF"
BLUE = "#0D1282"
FONT = "Courier"


# ---------------------------------------- PASSWORD GENERATOR ----------------------------------------
# Password Generator Project
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------------------- SAVE PASSWORD ----------------------------------------
def save_password():
    website = website_input.get().lower()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty."
        )
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, "end")
            password_input.delete(0, "end")


# ---------------------------------------- SEARCH PASSWORD ----------------------------------------
def find_password():
    try:
        website = website_input.get().lower()
        if website == "":
            messagebox.showinfo(
                title="Error",
                message="Type a website to search on data file.",
            )
            return

        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            website_data = data[website]
    except KeyError:
        messagebox.showerror(
            title="Oops",
            message=f"No details for {website.capitalize()} exists",
        )
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        messagebox.showinfo(
            title=f"{website.capitalize()}",
            message=f"Email: {website_data['email']}\nPassword: {website_data['password']}",
        )
    finally:
        website_input.delete(0, "end")


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
website_input = Entry()
website_input.grid(column=1, row=1)
website_input.focus()
email_input = Entry(width=36)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "rfjiq1986@gmail.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Buttons
search_button = Button(
    text="Search", width=12, highlightbackground=WHITE, command=find_password
)
search_button.grid(column=2, row=1)
generate_button = Button(
    text="Generate Password", highlightbackground=WHITE, command=generate_password
)
generate_button.grid(column=2, row=3)
add_button = Button(
    text="Add", width=36, highlightbackground=WHITE, command=save_password
)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
