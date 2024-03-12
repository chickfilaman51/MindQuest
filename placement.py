import tkinter as tk
import customtkinter as ctk
import rules

# Define questions for each grade
questions = {
    1: ["9 - 2 = ?", "13 + 4 = ?"],
    2: ["17 + 93 = ?", "132 - 74 = ?"],
    3: ["17 x 13 = ?", "621 / 27 = ?"],
    4: ["(28/7) / (6/7) = ?", "√49 = ?"],
    5: ["6.21 x 4.3 = ?", "8.3 x 32 = ?"],
    6: ["What is the volume of a rectangluar prism with sides of length 2, 3, and 5?","What is the hypotnuese of a right triangle with legs of length 5 and 12"],
    7: ["If 2(3x+4)=(4x+10)/3, what is x?","If (x/19)=2x-74, what is x?"],
    8: ["What is the greatest possible solution of x if 3x^2+4x+1=0","What is the product of the two solutions for x in this equation: 8x^2+45x+25=0"],
    9: ["The sum of two numbers is 18, and the product of these two numbers is 56. What is the larger of the two numbers?","Doug went to a conference in a city 120 km away. On the way back, due to road construction, he had to drive 10 km/h slower, which resulted in the return trip taking 2 hours longer.\nHow fast did he drive on the way to the conference?"],
    10: ["From a point on the ground 47 feet from the foot of a tree, the angle of elevation of the top of the tree is 35º. Find the height of the tree to the nearest foot.","An 8 foot metal guy wire is attached to a broken stop sign to secure its position until repairs can be made.\nAttached to a stake in the ground, the guy wire makes an angle of 51º with the ground. How far from the foot of the stop sign is the stake, to the nearest tenth of a foot?"]
    # Add questions for other grades similarly
}
answers = {
    1: [7,17],
    2: [110,58],
    3: [221,23],
    4: [14/3,7],
    5: [26.703,265.6],
    6: [30,13],
    7: [-1,38],
    8: [-1/3,25/8],
    9: [14,30],
    10: [33,5.0] 
}

# Initialize a dictionary to store the current question index for each grade
current_question_index = {}
question_num = 0

def display_next_question(grade):
    global question_num  # Declare question_num as a global variable
    grade_questions = questions.get(grade, [])
    if grade_questions:
        question_window = ctk.CTk()
        question_window.title(f"Grade {grade} - Question")
        question_window.geometry("400x200")
        question_window.attributes('-fullscreen', True)
        current_question_index.setdefault(grade, 0)  # Initialize the current question index if not already set
        current_question = grade_questions[current_question_index[grade]]
        num_label = ctk.CTkLabel(question_window, text=f"Question {grade + question_num}", font=("Arial", 15))
        question_label = ctk.CTkLabel(question_window, text=current_question, font=("Arial", 15))
        num_label.pack(pady= 15)
        question_label.pack(pady=10)
        question_label.place(relx=.5, rely=.35, anchor="c")
        question_label.place(relx=.5, rely=.45, anchor="c")

        # Function to handle the submission of the answer
        def submit_answer(answer):
            global question_num  # Use nonlocal to access the global question_num
            # Code to check the answer goes here
            print(f"Answer submitted: {answer}")
            # Display next question for the same grade
            if current_question_index[grade] + 1 < len(grade_questions):
                current_question_index[grade] += 1
                question_window.destroy()
                question_num += 1
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
        question_num = 0
        print(f"No questions available for Grade {grade}")

# Main function to start the placement test
def start_placement_test():
    for grade in range(1, 11):
        display_next_question(grade)

if __name__ == "__main__":
    start_placement_test()
