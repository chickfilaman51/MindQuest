import tkinter as tk
from tkinter import *
import customtkinter as ctk
import rules
from PIL import Image, ImageTk

# Set the appearance mode and color theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

# Create the main window
root = ctk.CTk()
root.title("Math App")
root.geometry("400x400")
root.attributes('-fullscreen', True)

# Defining image
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Load and resize the image
bgImage = Image.open("assets/forest.png")
bgImage = bgImage.resize((screen_width, screen_height))

# Making background
background_image = ImageTk.PhotoImage(bgImage)

# Create a Label widget to display the background image
background = Label(root, image=background_image)
background.place(x=0, y=0)

# Title label
title_label = ctk.CTkLabel(root, text="Mindquest", font=("Arial", 150, "bold"))
title_label.pack(pady=10)
title_label.place(relx=.5, rely=.45, anchor="c")

# Input field as a label
input_field = ctk.CTkLabel(root, text="Press Start to Begin Learning!", font=("Arial", 20))
input_field.pack(pady=10)
input_field.place(relx=.5, rely=.60, anchor="c")

# Start button
def destroy_and_open_rules():
    root.destroy()  # Destroy the current window
    rules.create_rules_window()  # Open the rules window

calculate_button = ctk.CTkButton(root, text="Start", command=destroy_and_open_rules)
calculate_button.pack(pady=10)
calculate_button.place(relx=.5, rely=.65, anchor="c")

# Run the main loop
if __name__ == "__main__":
    root.mainloop()
