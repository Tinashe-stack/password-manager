import json
import random
import string
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

import pyperclip

DATA_FILE = Path("data.json")
DEFAULT_EMAIL = "username@hotmail.co.uk"
PASSWORD_LENGTH_RANGE = (12, 18)
SYMBOLS = "!#$%&()*+"


class PasswordManagerApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Password Manager")
        self.root.config(padx=50, pady=50)
        self.root.resizable(False, False)

        self.website_entry: tk.Entry
        self.email_entry: tk.Entry
        self.password_entry: tk.Entry
        self.logo_image = None

        self._build_ui()

    def _build_ui(self) -> None:
        # Logo / header
        canvas = tk.Canvas(self.root, width=200, height=200, highlightthickness=0)
        try:
            self.logo_image = tk.PhotoImage(file="logo.png")
            canvas.create_image(100, 100, image=self.logo_image)
        except tk.TclError:
            # Fallback if logo.png is missing
            canvas.create_text(
                100,
                100,
                text="Password\nManager",
                font=("Arial", 20, "bold"),
            )
        canvas.grid(row=0, column=1, pady=(0, 20))

        # Website row
        website_label = tk.Label(self.root, text="Website:")
        website_label.grid(row=1, column=0, sticky="e", padx=(0, 8), pady=5)

        self.website_entry = tk.Entry(self.root, width=21)
        self.website_entry.grid(row=1, column=1, sticky="ew", pady=5)
        self.website_entry.focus()

        search_button = tk.Button(
            self.root,
            text="Search",
            width=13,
            command=self.find_password,
        )
        search_button.grid(row=1, column=2, pady=5)

        # Email row
        email_label = tk.Label(self.root, text="Email/Username:")
        email_label.grid(row=2, column=0, sticky="e", padx=(0, 8), pady=5)

        self.email_entry = tk.Entry(self.root, width=35)
        self.email_entry.grid(row=2, column=1, columnspan=2, sticky="ew", pady=5)
        self.email_entry.insert(0, DEFAULT_EMAIL)

        # Password row
        password_label = tk.Label(self.root, text="Password:")
        password_label.grid(row=3, column=0, sticky="e", padx=(0, 8), pady=5)

        self.password_entry = tk.Entry(self.root, width=21)
        self.password_entry.grid(row=3, column=1, sticky="ew", pady=5)

        generate_button = tk.Button(
            self.root,
            text="Generate Password",
            command=self.generate_password,
        )
        generate_button.grid(row=3, column=2, pady=5)

        # Add button
        add_button = tk.Button(
            self.root,
            text="Add",
            width=36,
            command=self.save_password,
        )
        add_button.grid(row=4, column=1, columnspan=2, pady=(10, 0))

    def generate_password(self) -> None:
        length = random.randint(*PASSWORD_LENGTH_RANGE)
        characters = string.ascii_letters + string.digits + SYMBOLS
        password = "".join(random.choice(characters) for _ in range(length))

        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        pyperclip.copy(password)

    def save_password(self) -> None:
        website = self.website_entry.get().strip().title()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not website or not email or not password:
            messagebox.showerror(
                title="Oops",
                message="Please don't leave any fields empty.",
            )
            return

        new_data = {website: {"email": email, "password": password}}

        is_ok = messagebox.askokcancel(
            title=website,
            message=(
                "These are the details entered:\n"
                f"Email: {email}\n"
                f"Password: {password}\n\n"
                "Is it okay to save?"
            ),
        )
        if not is_ok:
            return

        data = self._load_data()
        data.update(new_data)
        self._save_data(data)

        self.website_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.website_entry.focus()

        messagebox.showinfo(
            title="Saved",
            message=f"Credentials for {website} were saved successfully.",
        )

    def find_password(self) -> None:
        website = self.website_entry.get().strip().title()
        if not website:
            messagebox.showerror(
                title="Oops",
                message="Please enter a website name to search.",
            )
            return

        data = self._load_data()
        if not data:
            messagebox.showinfo(
                title="Error",
                message="No data file found or no saved credentials available.",
            )
            return

        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            pyperclip.copy(password)
            messagebox.showinfo(
                title=website,
                message=(
                    f"Email: {email}\n"
                    f"Password: {password}\n\n"
                    "The password has been copied to your clipboard."
                ),
            )
        else:
            messagebox.showinfo(
                title="Not found",
                message=f"No details for {website} exist.",
            )

    def _load_data(self) -> dict:
        if not DATA_FILE.exists():
            return {}

        try:
            with DATA_FILE.open("r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            messagebox.showerror(
                title="Data Error",
                message=(
                    "The data file is corrupted or contains invalid JSON.\n"
                    "Please fix or replace data.json."
                ),
            )
            return {}

    def _save_data(self, data: dict) -> None:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)


def main() -> None:
    root = tk.Tk()
    PasswordManagerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()