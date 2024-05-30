import tkinter as tk
from PIL import Image, ImageTk
import pygame

def home_page():
    root = tk.Tk()
    root.title("Learn Urdu")
    root.geometry("1250x600")
    root.configure(background='dark turquoise')

    def exit_program():
        pygame.mixer.quit()
        root.destroy()

    def learn_alphabet():
        clear_screen()
        img = Image.open("Urdu.png")
        photo = ImageTk.PhotoImage(img)

        img_label = tk.Label(root, image=photo, bg='dark turquoise')
        img_label.image = photo  
        img_label.pack(pady=20)

        def play_audio():
            pygame.mixer.init()
            pygame.mixer.music.load("alphabet_audio.mp3")
            pygame.mixer.music.play()

        audio_img = Image.open("audio.png").resize((50, 50))
        audio_photo = ImageTk.PhotoImage(audio_img)
        audio_button = tk.Button(root, image=audio_photo, command=play_audio, bg='dark turquoise')
        audio_button.image = audio_photo
        audio_button.pack(pady=10)

        back_button = tk.Button(root, text="Back", command=reset_to_home_page,
                                font=("Comic Sans MS", 20),
                                bg='darkblue',
                                fg='dark turquoise',
                                relief="raised",
                                borderwidth=2)
        back_button.pack(pady=10)
    
    def clear_screen():
        for widget in root.winfo_children():
            widget.destroy()

    def start_quiz():
        clear_screen()
        # Quiz code here

    def reset_to_home_page():
        clear_screen()
        setup_home_page()

    def setup_home_page():
        label1 = tk.Label(root, text="Learn the Urdu Alphabet",
                          font=("Source Sans Pro", 40),
                          bg='dark turquoise',
                          fg='darkblue',
                          padx=20,
                          pady=10,
                          relief="flat",
                          borderwidth=2)
        label1.pack(pady=20)

        img_urdu = Image.open("Urdu1.png")
        photo_urdu = ImageTk.PhotoImage(img_urdu)

        img_label_center = tk.Label(root, image=photo_urdu, bg='dark turquoise')
        img_label_center.image = photo_urdu
        img_label_center.pack(pady=20)

        button_frame = tk.Frame(root, bg='dark turquoise')
        button_frame.pack(pady=20)

    setup_home_page()
    root.mainloop()

home_page()
