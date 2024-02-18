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
title_label = ctk.CTkLabel(root, text="Math App", font=("Arial",  16, "bold"))
title_label.pack(pady=10)

# Input field
input_field = ctk.CTkEntry(root, placeholder_text="Enter math expression")
input_field.pack(pady=10)

# Calculate button
calculate_button = ctk.CTkButton(root, text="Calculate", command=lambda: calculate(input_field.get()))
calculate_button.pack(pady=10)

# Result label
result_label = ctk.CTkLabel(root, text="Result:", font=("Arial",  14))
result_label.pack(pady=10)

# Display result
result_display = ctk.CTkLabel(root, text="", font=("Arial",  14))
result_display.pack(pady=10)

# Calculation logic
def calculate(expression):
    try:
        result = eval(expression)
        result_display.config(text=str(result))
    except Exception as e:
        result_display.config(text="Invalid expression")

# Run the main loop
root.mainloop()
