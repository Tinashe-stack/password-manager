# Password Manager

A Python desktop application built with Tkinter for generating strong passwords, storing credentials locally, and searching saved login details.

## Overview

This project was built to practise Python GUI development, file handling, JSON data storage, and user-focused application design. The app allows a user to generate secure passwords, copy them to the clipboard automatically, and save website credentials for later lookup.

## Features

- Generate random passwords using letters, numbers, and symbols.
- Automatically copy generated passwords to the clipboard.
- Save website, email/username, and password details to a local `data.json` file.
- Search saved credentials by website name.
- Simple Tkinter interface for quick desktop use.

## Tech Stack

- Python 3
- Tkinter
- `pyperclip`
- `json`
- `random`

## Project Structure

- `main.py` — main application logic and Tkinter UI.
- `logo.png` — application logo displayed in the interface.
- `data.json` — local file used to store saved credentials.

## Installation

1. Clone the repository.
2. Install the required dependency:

```bash
pip install pyperclip
```

3. Run the application:

```bash
python main.py
```

## How to Use

1. Enter a website name.
2. Enter an email address or username.
3. Click **Generate Password** to create a password.
4. Click **Add** to save the credentials.
5. Use **Search** to look up saved credentials for a website.

## What I Learned

This project helped me improve my understanding of:

- Python GUI development with Tkinter.
- Working with structured data using JSON.
- Input validation and user feedback with message boxes.
- Building small desktop tools with practical functionality.

## Limitations

This project stores credentials locally in a JSON file and is intended as a learning project rather than a production-ready password manager. A stronger future version could include encryption, update/delete functionality, and automated tests.

## Future Improvements

- Encrypt stored credentials.
- Add update and delete entry features.
- Improve error handling for corrupted or missing data files.
- Refactor the code into smaller functions or modules.
- Add unit tests for password generation and file operations.

## Screenshot

![Password Manager](screenshot.png)

---

Built as part of my Python learning journey and portfolio development.
