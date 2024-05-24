from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Learn Urdu")
root.geometry("800x600")
root.configure(background="lightblue")

def home_page():
    for widget in root.winfo_children():
        widget.destroy()

    # Title Label
    Label1 = Label(root, text="Learn the Urdu Alphabet",
                   font=("Source Sans Pro", 30),
                   bg="lightblue",
                   fg="darkblue",
                   padx=20,
                   pady=10,
                   relief="flat",
                   borderwidth=2)
    Label1.pack(pady=20)

    # Load images
    img_pakistan = Image.open("pakistan.png")
    img_pakistan = img_pakistan.resize((200, 200), Image.Resampling.LANCZOS)
    photo_pakistan = ImageTk.PhotoImage(img_pakistan)

    img_urdu = Image.open("Urdu1.png")
    img_urdu = img_urdu.resize((200, 200), Image.Resampling.LANCZOS)
    photo_urdu = ImageTk.PhotoImage(img_urdu)

    # Create a frame to hold the images and buttons
    main_frame = Frame(root, bg="lightblue")
    main_frame.pack(expand=True)

    # Place images in labels
    img_label_left = Label(main_frame, image=photo_pakistan, bg="lightblue")
    img_label_left.image = photo_pakistan  # keep a reference!
    img_label_left.grid(row=0, column=0, padx=20, pady=100)

    img_label_right = Label(main_frame, image=photo_urdu, bg="lightblue")
    img_label_right.image = photo_urdu  # keep a reference!
    img_label_right.grid(row=0, column=2, padx=20, pady=100)

    # Create a frame to hold the buttons
    button_frame = Frame(main_frame, bg="lightblue")
    button_frame.grid(row=0, column=1, padx=20, pady=100)

    # Buttons
    button1 = Button(button_frame, text="Learn the Alphabet", command=learn_alphabet,
                     font=("Comic Sans MS", 15),
                     bg="darkblue",
                     fg="lightblue",
                     relief="raised",
                     borderwidth=2)
    button1.pack(pady=10)

    button2 = Button(button_frame, text="Start Quiz", command=start_quiz,
                     font=("Comic Sans MS", 15),
                     bg="darkblue",
                     fg="lightblue",
                     relief="raised",
                     borderwidth=2)
    button2.pack(pady=10)

def learn_alphabet():
    for widget in root.winfo_children():
        widget.destroy()

    img = Image.open("Urdu.png")
    img = img.resize((500, 400), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)

    img_label = Label(root, image=photo)
    img_label.image = photo  # keep a reference!
    img_label.pack(pady=20)

    back_button = Button(root, text="Back", command=home_page,
                         font=("Comic Sans MS", 15),
                         bg="darkblue",
                         fg="lightblue",
                         relief="raised",
                         borderwidth=2)
    back_button.pack(pady=20)

def start_quiz():
    for widget in root.winfo_children():
        widget.destroy()

    current_question = 1
    score = 0

    def next_question():
        nonlocal current_question
        if current_question <= 10:
            question_label.config(text=f"Q{current_question}: Put question {current_question} here")
            if current_question % 2 == 1:
                answer_entry.pack_forget()
                answer_radio1.pack()
                answer_radio2.pack()
                answer_radio3.pack()
                answer_radio4.pack()
            else:
                answer_radio1.pack_forget()
                answer_radio2.pack_forget()
                answer_radio3.pack_forget()
                answer_radio4.pack_forget()
                answer_entry.pack()
            current_question += 1
        else:
            for widget in root.winfo_children():
                widget.destroy()
            score_label = Label(root, text=f"Final Score: {score}/10", font=("Comic Sans MS", 20))
            score_label.pack(pady=20)
            back_button = Button(root, text="Back to Home", command=home_page,
                                 font=("Comic Sans MS", 15),
                                 bg="darkblue",
                                 fg="lightblue",
                                 relief="raised",
                                 borderwidth=2)
            back_button.pack(pady=20)

    def submit_answer():
        nonlocal score
        if current_question % 2 == 1:
            selected = answer_var.get()
            # Check if selected answer is correct (example: correct answer is always option 1)
            if selected == 1:
                feedback_label.config(text="Correct!")
                score += 1
            else:
                feedback_label.config(text="Incorrect!")
        else:
            user_answer = answer_entry.get()
            # Check if entered answer is correct (example: correct answer is always 'A')
            if user_answer.lower() == 'a':
                feedback_label.config(text="Correct!")
                score += 1
            else:
                feedback_label.config(text="Incorrect!")
    
    question_label = Label(root, text="Q1: Put question 1 here", font=("Comic Sans MS", 20))
    question_label.pack(pady=20)

    answer_var = IntVar()

    answer_radio1 = Radiobutton(root, text="Option 1", variable=answer_var, value=1)
    answer_radio2 = Radiobutton(root, text="Option 2", variable=answer_var, value=2)
    answer_radio3 = Radiobutton(root, text="Option 3", variable=answer_var, value=3)
    answer_radio4 = Radiobutton(root, text="Option 4", variable=answer_var, value=4)

    answer_radio1.pack()
    answer_radio2.pack()
    answer_radio3.pack()
    answer_radio4.pack()

    answer_entry = Entry(root, font=("Comic Sans MS", 15))
    feedback_label = Label(root, text="", font=("Comic Sans MS", 15))
    feedback_label.pack(pady=10)

    submit_button = Button(root, text="Submit Answer", command=submit_answer,
                           font=("Comic Sans MS", 15),
                           bg="darkblue",
                           fg="lightblue",
                           relief="raised",
                           borderwidth=2)
    submit_button.pack(pady=10)

    next_button = Button(root, text="Next Question", command=next_question,
                         font=("Comic Sans MS", 15),
                         bg="darkblue",
                         fg="lightblue",
                         relief="raised",
                         borderwidth=2)
    next_button.pack(pady=10)

home_page()

root.mainloop()
