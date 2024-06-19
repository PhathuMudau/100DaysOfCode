import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD SEARCH ------------------------------- #


def search_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            web_data = data[website]
    except FileNotFoundError:
        messagebox.showinfo(title="File Error", message="Data file not found")
    except KeyError:
        messagebox.showinfo(title="Search Error", message=f"Details for {website} not found in file. Search is case "
                                                          f"sensitive, using 'Title Case'")
    else:
        web_user = web_data["email"]
        web_pass = web_data["password"]
        messagebox.showinfo(title=website, message=f"Email: {web_user} \nPassword: {web_pass}")
        pyperclip.copy(web_pass)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for n in range(randint(8, 10))]
    number_list = [choice(numbers) for n in range(randint(2, 4))]
    symbol_list = [choice(symbols) for n in range(randint(2, 4))]

    password_list = letter_list + number_list + symbol_list
    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    email = email_input.get()
    website = website_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please ensure all the fields are populated")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image_bg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_bg)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
website_input = Entry(width=33)
website_input.grid(row=1, column=1)
website_input.focus()

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
email_input = Entry(width=53)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "phathu.mudau@yahoo.com")

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)
password_input = Entry(width=33)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(row=3, column=2)

search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(row=1, column=2)

add_button = Button(text="Add", width=45, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)






window.mainloop()
