import tkinter as tk
import customtkinter as ctk

# Set the appearance mode and color theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

# Create the main window
root = ctk.CTk()
root.title("Math App")
root.geometry("400x400")

# Title label
title_label = ctk.CTkLabel(root, text="Mindquest", font=("Arial",  16, "bold"))
title_label.pack(pady=10)

# Input field as a label
input_field = ctk.CTkLabel(root, text="Press Start to Begin Learning!")
input_field.pack(pady=10)

# Start button
calculate_button = ctk.CTkButton(root, text="Start")
calculate_button.pack(pady=10)

# Run the main loop
if __name__ == "__main__":
    root.mainloop()
import tkinter as tk
import customtkinter as ctk

# Set the appearance mode and color theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

# Create the main window
root = ctk.CTk()
root.title("Math App")
root.geometry("400x400")

# Title label
title_label = ctk.CTkLabel(root, text="Mindquest", font=("Arial",  16, "bold"))
title_label.pack(pady=10)

# Input field as a label
input_field = ctk.CTkLabel(root, text="Press Start to Begin Learning!")
input_field.pack(pady=10)

# Start button
calculate_button = ctk.CTkButton(root, text="Start")
calculate_button.pack(pady=10)

# Run the main loop
if __name__ == "__main__":
    root.mainloop()
