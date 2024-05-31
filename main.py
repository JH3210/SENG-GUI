import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame

def home_page():
    root = tk.Tk()
    root.title("Learn Urdu")
    root.geometry("1250x600")
    root.configure(background='lime green')

    def exit_program():
        root.destroy()

    def learn_alphabet():
        clear_screen()
        img = Image.open("Urdu.png")
        photo = ImageTk.PhotoImage(img)

        img_label = tk.Label(root, image=photo, bg='lime green')
        img_label.image = photo  
        img_label.pack(pady=20)

        def play_audio():
            pygame.mixer.init()
            pygame.mixer.music.load("alphabet_audio.mp3")
            pygame.mixer.music.play()

        audio_img = Image.open("audio.png").resize((50, 50))
        audio_photo = ImageTk.PhotoImage(audio_img)
        audio_button = tk.Button(root, image=audio_photo, command=play_audio, bg='lime green')
        audio_button.image = audio_photo
        audio_button.pack(pady=10)

        back_button = tk.Button(root, text="Back", command=reset_to_home_page,
                                font=("Arial", 20),
                                bg='RoyalBlue3',
                                fg='lime green',
                                relief="raised",
                                borderwidth=2)
        back_button.pack(pady=20)
    
    def clear_screen():
        for widget in root.winfo_children():
            widget.destroy()

    def start_quiz():
        clear_screen()
        current_question = 0
        score = 0

        questions = [
            "What is the first letter of the Urdu alphabet?",
            "How is this letter pronounced in Urdu - م (Write your answer in English transliteration)",
            "Which letter is pronounced as 'Jeem'?",
            "True or False : ے (Bari Ye) is the last letter of the Urdu Alphabet",
            "Which letter is pronounced 'Noon' in Urdu?",
            "What is the letter ر in transliteration?",
            "What is the letter چ in transliteration?",
            "True or False : The urdu language has 39 letters in total",
            "Which of these options, when pronounced in English, starts with an L?",
            "What number place of the alphabet does ا (Alif) come in? (Type only the number)"
        ]

        options = [
             ["ا (Alif)", "ب (Bay)", "پ (Pay)", "ت (Tay)"],
             [],
             ["ج", "چ ", "ح ", "خ "],
             [],
             ["ن", "م", "ل", "ک"],
             [],
             ["Jeem", "Chay", "Khay", "Ray"],
             [],
             ["ل", "ط", "س", "ف"],
             []
        ]

        correct_answers = ["1", "meem", "1", "true", "1", "ray", "2", "true", "1", "1"]

        def show_question():
            question_label.config(text=f"Q{current_question + 1}: {questions[current_question]}")
            if current_question in [0, 2, 4, 6, 8]:
                show_radio_buttons()
            else:
                show_entry()

        def show_radio_buttons():
            answer_radio1.config(text=options[current_question][0])
            answer_radio2.config(text=options[current_question][1])
            answer_radio3.config(text=options[current_question][2])
            answer_radio4.config(text=options[current_question][3])
            answer_radio1.pack(pady=5)
            answer_radio2.pack(pady=5)
            answer_radio3.pack(pady=5)
            answer_radio4.pack(pady=5)
            entry_answer.pack_forget()

        def show_entry():
            entry_answer.pack(pady=2)
            answer_radio1.pack_forget()
            answer_radio2.pack_forget()
            answer_radio3.pack_forget()
            answer_radio4.pack_forget()

        def check_answer():
            selected = None
            if current_question in [0, 2, 4, 6, 8]:
                selected = str(answer.get())
            else:
                selected = entry_answer.get().strip().lower()  
            
            if selected == correct_answers[current_question].lower():  
                messagebox.showinfo("Result", "Correct!")
                nonlocal score
                score += 1
            else:
                messagebox.showinfo("Result", "Incorrect!")

        def next_question():
            nonlocal current_question
            if current_question < 10:
                check_answer()
                current_question += 1
                if current_question < 10:  
                    entry_answer.delete(0, tk.END)  
                    show_question()
                else:  
                    clear_screen()
                    score_label = tk.Label(root, text=f"Final Score: {score}/10", font=("Arial", 20), bg='lime green')
                    score_label.pack(pady=20)  
                    back_button = tk.Button(root, text="Back to Home", command=reset_to_home_page,
                                            font=("Arial", 20),
                                            bg='RoyalBlue3',
                                            fg='lime green',
                                            relief="raised",
                                            borderwidth=2)
                    back_button.pack(pady=20)  

        question_frame = tk.Frame(root, bg='lime green')
        question_frame.pack(pady=20)

        question_label = tk.Label(question_frame, text="", font=("Arial", 20), bg='lime green')
        question_label.pack(pady=20)

        answer = tk.IntVar()

        answer_radio1 = tk.Radiobutton(question_frame, variable=answer, value=1, font=("Arial", 15), bg='lime green')
        answer_radio2 = tk.Radiobutton(question_frame, variable=answer, value=2, font=("Arial", 15), bg='lime green')
        answer_radio3 = tk.Radiobutton(question_frame, variable=answer, value=3, font=("Arial", 15), bg='lime green')
        answer_radio4 = tk.Radiobutton(question_frame, variable=answer, value=4, font=("Arial", 15), bg='lime green')

        entry_answer = tk.Entry(question_frame, font=("Arial", 15))

        answer_radio1.pack(pady=5)
        answer_radio2.pack(pady=5)
        answer_radio3.pack(pady=5)
        answer_radio4.pack(pady=5)

        next_button = tk.Button(root, text="Next", command=next_question,
                                font=("Arial", 20),
                                bg='RoyalBlue3',
                                fg='lime green',
                                relief="raised",
                                borderwidth=2)
        next_button.pack(pady=20)

        show_question()

    def reset_to_home_page():
        for widget in root.winfo_children():
            widget.destroy()
        setup_home_page()

    def setup_home_page():
        label1 = tk.Label(root, text="Learn the Urdu Alphabet",
                          font=("Impact", 60),
                          bg='lime green',
                          fg='RoyalBlue3',
                          padx=20,
                          pady=10,
                          relief="flat",
                          borderwidth=2)
        label1.pack(pady=20)

        img_urdu = Image.open("Urdu1.png")
        photo_urdu = ImageTk.PhotoImage(img_urdu)

        img_label_center = tk.Label(root, image=photo_urdu, bg='lime green')
        img_label_center.image = photo_urdu
        img_label_center.pack(pady=20)

        button_frame = tk.Frame(root, bg='lime green')
        button_frame.pack(pady=20)

        button1 = tk.Button(button_frame, text="Learn the Alphabet", command=learn_alphabet,
                            font=("Arial", 20),
                            bg='RoyalBlue3',
                            fg='lime green',
                            relief="raised",
                            borderwidth=2,
                            width=20)
        button1.pack(side=tk.LEFT, padx=10)

        button2 = tk.Button(button_frame, text="Start Quiz", command=start_quiz,
                            font=("Arial", 20),
                            bg='RoyalBlue3',
                            fg='lime green',
                            relief="raised",
                            borderwidth=2,
                            width=20)
        button2.pack(side=tk.LEFT, padx=10)

        button3 = tk.Button(button_frame, text="Exit", command=exit_program,
                            font=("Arial", 20),
                            bg='RoyalBlue3',
                            fg='lime green',
                            relief="raised",
                            borderwidth=2,
                            width=20)
        button3.pack(side=tk.LEFT, padx=10)

    setup_home_page()
    root.mainloop()

home_page()
