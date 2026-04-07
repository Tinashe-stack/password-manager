from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

   
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)  # Removed duplicate shuffle

    password = "".join(password_list)
    word.delete(0, END)  # Clear before inserting
    word.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web.get().strip().title()
    email = mail.get().strip()
    password = word.get().strip()

    if not website or not email or not password:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
        return

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?"
    )

    if not is_ok:
        return

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    web.delete(0, END)
    word.delete(0, END)
    web.focus()


def find_password():
    website = web.get().strip().title()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)  # Slightly more padding

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")  # Variable name for clarity
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website
website_label = Label(text="Website:", font=("Arial", 10))
website_label.grid(row=1, column=0, sticky="e")
web = Entry(width=21)
web.grid(row=1, column=1, sticky="ew")
web.focus()

# Email
email_label = Label(text="Email/Username:", font=("Arial", 10))
email_label.grid(row=2, column=0, sticky="e")
mail = Entry(width=35)
mail.insert(0, "username@hotmail.co.uk")
mail.grid(row=2, column=1, columnspan=2, sticky="ew")

# Password
password_label = Label(text="Password:", font=("Arial", 10))
password_label.grid(row=3, column=0, sticky="e")
word = Entry(width=21)
word.grid(row=3, column=1, sticky="ew")

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=3, column=2)

search_btn = Button(text="Search", width=13, command=find_password)
search_btn.grid(row=1, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()
