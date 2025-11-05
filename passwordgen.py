import tkinter as tk
from tkinter import messagebox
import random
import string
import os
from datetime import datetime

def generate_password(length, use_letters, use_numbers, use_symbols):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    
    characters = ""
    if use_letters:
        characters += letters
    if use_numbers:
        characters += numbers
    if use_symbols:
        characters += symbols

    if not characters:
        return None, "Error: Select at least one character type."

    if length <= 0:
        return None, "Error: Length must be greater than zero."

    password = ''.join(random.choice(characters) for _ in range(length))
    
    required_chars = []
    if use_letters and any(char in characters for char in letters):
        required_chars.append(random.choice(letters))
    if use_numbers and any(char in characters for char in numbers):
        required_chars.append(random.choice(numbers))
    if use_symbols and any(char in characters for char in symbols):
        required_chars.append(random.choice(symbols))

    if required_chars and length >= len(required_chars):
        password_list = list(password)
        random.shuffle(password_list) 
        
        for i in range(len(required_chars)):
            if i < len(password_list):
                 password_list[i] = required_chars[i]

        random.shuffle(password_list) 
        password = ''.join(password_list)

    return password, "Password generated and saved!"

def save_password(password):
    FOLDER_NAME = "passwords"
    FILE_NAME = "generated_passwords.txt"
    
    try:
        os.makedirs(FOLDER_NAME, exist_ok=True)
    except OSError as e:
        return f"Error: Could not create folder '{FOLDER_NAME}'. ({e})"

    file_path = os.path.join(FOLDER_NAME, FILE_NAME)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Length: {len(password)}, Password: {password}\n"
    
    try:
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(log_entry)
        return "Password saved successfully."
    except Exception as e:
        return f"Error: Could not save password to file. ({e})"

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator (GUI)")
        master.resizable(False, False)

        
        self.length_var = tk.StringVar(master, value='12')
        self.letters_var = tk.BooleanVar(master, value=True)
        self.numbers_var = tk.BooleanVar(master, value=True)
        self.symbols_var = tk.BooleanVar(master, value=True)
        self.password_var = tk.StringVar(master, value='Click "Generate" to create a password.')
        self.status_var = tk.StringVar(master, value='')

        tk.Label(master, text="Password Length:", font=('Arial', 10)).grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        self.length_entry = tk.Entry(master, textvariable=self.length_var, width=5, font=('Arial', 10))
        self.length_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        options_frame = tk.LabelFrame(master, text="Select Characters:", padx=10, pady=10, font=('Arial', 10, 'bold'))
        options_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='ew')
        
        tk.Checkbutton(options_frame, text="Letters (aA-zZ)", variable=self.letters_var, font=('Arial', 10)).pack(anchor='w')
        tk.Checkbutton(options_frame, text="Numbers (0-9)", variable=self.numbers_var, font=('Arial', 10)).pack(anchor='w')
        tk.Checkbutton(options_frame, text="Symbols (!@#$)", variable=self.symbols_var, font=('Arial', 10)).pack(anchor='w')

        tk.Button(master, text="GENERATE AND SAVE PASSWORD", command=self.generate_and_save, 
                  bg='#4CAF50', fg='white', font=('Arial', 10, 'bold')).grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

        tk.Label(master, text="Generated Password:", font=('Arial', 10)).grid(row=3, column=0, padx=10, pady=(10, 0), sticky='w')
        self.password_display = tk.Entry(master, textvariable=self.password_var, width=40, state='readonly', 
                                         font=('Courier', 10))
        self.password_display.grid(row=4, column=0, columnspan=2, padx=10, pady=(0, 10), sticky='ew')
        
        tk.Label(master, textvariable=self.status_var, fg='blue', font=('Arial', 9)).grid(row=5, column=0, columnspan=2, sticky='w', padx=10)

       
        tk.Label(master, text="Made By Exif", font=('Arial', 7), fg='gray').grid(row=6, column=0, sticky='sw', padx=5, pady=5)

    def generate_and_save(self):
        try:
            length = int(self.length_var.get())
        except ValueError:
            messagebox.showerror("Error", "Length must be an integer.")
            return

        use_letters = self.letters_var.get()
        use_numbers = self.numbers_var.get()
        use_symbols = self.symbols_var.get()

        password, status_message = generate_password(length, use_letters, use_numbers, use_symbols)

        if password:
            self.password_var.set(password)
            save_status = save_password(password)
            self.status_var.set(f"{status_message} {save_status}")
        else:
            self.password_var.set("Error generating password.")
            self.status_var.set(status_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()