import tkinter as tk
import customtkinter as ctk
import rules
# Define questions for each grade
questions = {
    1: ["1 + 1 = ?", "2 + 3 = ?"],
    2: ["10 - 3 = ?", "5 * 2 = ?"],
    3: ["15 / 3 = ?", "7 + 4 = ?"],
    # Add questions for other grades similarly
}

# Initialize a dictionary to store the current question index for each grade
current_question_index = {}

def display_next_question(grade):
    grade_questions = questions.get(grade, [])
    if grade_questions:
        question_window = ctk.CTk()
        question_window.title(f"Grade {grade} - Question")
        question_window.geometry("400x200")
        question_window.attributes('-fullscreen', True)
        current_question_index.setdefault(grade, 0)  # Initialize the current question index if not already set
        current_question = grade_questions[current_question_index[grade]]
        question_label = ctk.CTkLabel(question_window, text=current_question, font=("Arial", 15))
        question_label.pack(pady=10)
        question_label.place(relx=.5, rely=.45, anchor="c")

        # Function to handle the submission of the answer
        def submit_answer(answer):
            # Code to check the answer goes here
            print(f"Answer submitted: {answer}")
            # Display next question for the same grade
            if current_question_index[grade] + 1 < len(grade_questions):
                current_question_index[grade] += 1
                display_next_question(grade)
            else:
                print("No more questions for this grade")
            question_window.destroy()

        # Answer entry field
        answer_entry = ctk.CTkEntry(question_window)
        answer_entry.pack(pady=10)
        answer_entry.place(relx=.5, rely=.65, anchor="c")

        # Submit button
        submit_button = ctk.CTkButton(question_window, text="Submit", command=lambda: submit_answer(answer_entry.get()))
        submit_button.pack(pady=10)
        submit_button.place(relx=.5, rely=.75, anchor="c")

        question_window.mainloop()
    else:
        print(f"No questions available for Grade {grade}")

# Main function to start the placement test
def start_placement_test():
    for grade in range(1, 11):
        display_next_question(grade)

if __name__ == "__main__":
    start_placement_test()
