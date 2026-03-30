from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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
    if not web.get() or not mail.get() or not word.get():
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web.get(), 
        message=f"Website: {web.get()}\nEmail: {mail.get()}\nPassword: {word.get()}\nIs it OK to save?")
        if is_ok:
            with open("passwords.txt", "a") as file:  # Safer filename
                file.write(f"{web.get()} | {mail.get()} | {word.get()}\n")
            web.delete(0, END)
            mail.delete(0, END)  # Clear email too
            word.delete(0, END)

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
web = Entry(width=35)
web.grid(row=1, column=1, columnspan=2, sticky="ew")
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

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()
