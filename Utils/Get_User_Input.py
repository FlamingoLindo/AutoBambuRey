import customtkinter as tk
from tkinter import simpledialog

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window
    user_input = simpledialog.askstring("Input", prompt)
    return user_input