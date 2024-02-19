import tkinter as tk
import customtkinter as ctk
import rules
# Set the appearance mode and color theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

# Create the main window
root = ctk.CTk()
root.title("Math App")
root.geometry("400x400")

root.attributes('-fullscreen', True)

# Title label
title_label = ctk.CTkLabel(root, text="Mindquest", font=("Arial",  150, "bold"))
title_label.pack(pady=10)
title_label.place(relx=.5, rely=.45, anchor="c")
# Input field as a label
input_field = ctk.CTkLabel(root, text="Press Start to Begin Learning!", font=("Arial",  20))
input_field.pack(pady=10)
input_field.place(relx=.5, rely=.60, anchor="c")

# Start button
calculate_button = ctk.CTkButton(root, text="Start", command=rules.create_rules_window)
calculate_button.pack(pady=10)
calculate_button.place(relx=.5, rely=.65, anchor="c")


# Run the main loop
if __name__ == "__main__":
    root.mainloop()
