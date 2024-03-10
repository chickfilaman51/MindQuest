import tkinter as tk
import customtkinter as ctk
import placement
from tkinter import*
from PIL import Image,ImageTk

# Function to show the placement test window
    

# Create the rules window
def create_rules_window():
    # Destroy the current window if it exists
    global rules_window
    rules_window = ctk.CTk()
    rules_window.title("Rules")
    rules_window.geometry("400x400")
    rules_window.attributes('-fullscreen', True)
    #Image
    screen_width=rules_window.winfo_screenwidth()
    screen_height=rules_window.winfo_screenheight()
    bg=Image.open("assets/forest.png")
    bg=bg.resize((screen_width,screen_height))
    background_im=ImageTk.PhotoImage(bg)
    background = Label(rules_window,image=background_im)
    background.place(x=0,y=0)
    # Add rules text here
    rules_label = ctk.CTkLabel(rules_window, text="This app is dedicated to helping people that have trouble learning in school.\nThis app uses fun activities, while still allowing kids to learn.\nBy clicking this button, you will be automatically sent to a placement test where you will be tested on how much knowledge you already have when it comes to math", font=("Arial",  15))
    rules_label.pack(pady=10)
    rules_label.place(relx=.5, rely=.45, anchor="c")
    # Placement test button
    placement_button = ctk.CTkButton(rules_window, text="Start Placement Test", command=show_placement_test)
    placement_button.pack(pady=10)
    placement_button.place(relx=.5, rely=.65, anchor="c")
    rules_window.mainloop()

def show_placement_test():
        rules_window.destroy()
        placement.start_placement_test()

# Run the function to create the rules window
if __name__ == "__main__":
    create_rules_window()
