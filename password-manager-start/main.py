from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]

    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("passwords.json", "r") as file:
                # json.dump(new_data, file, indent=4)
                data = json.load(file)
        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
        data_website = data[website]
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No File Found")
    except KeyError:
        messagebox.showinfo(title="Oops", message="No details for the website")
    else:
        messagebox.showinfo(title=website, message=f"Email: {data_website['email']} "
                                                   f"\nPassword: {data_website['password']}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_name = Label(text="Email/Username:")
email_name.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "ahmed@email.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

window.mainloop()
