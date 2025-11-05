# 🔒 Secure Password Generator

This is a simple, yet robust desktop application built with Python and Tkinter, designed to generate strong, customizable passwords and securely log them to a local file.

## ✨ Features

* **Graphical User Interface (GUI):** Easy-to-use interface built with the standard Python library, Tkinter.
* **Customizable Length:** Define the desired length of the password.
* **Character Selection:** Choose whether to include letters (A-Z, a-z), numbers (0-9), and special symbols (!@#$%...).
* **Guaranteed Complexity:** Ensures the generated password includes at least one character of each selected type for maximum strength.
* **Local Secure Logging:** Automatically creates a `passwords` folder and saves all generated passwords, along with a timestamp and length, in a file named `generated_passwords.txt`.


## 🚀 Getting Started

### Prerequisites

You only need a working installation of **Python 3.x**. All libraries used (`tkinter`, `random`, `string`, `os`, `datetime`) are built into the standard Python installation.
