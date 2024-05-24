import tkinter as tk
from PIL import Image, ImageTk

def home_page():
    root = tk.Tk()
    root.title("Learn Urdu")
    root.geometry("800x600")
    root.configure(background='lightblue')

    def exit_program():
        root.destroy()

    def learn_alphabet():
        clear_screen()
        img = Image.open("Urdu.png")
        img = img.resize((600, 500), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)

        img_label = tk.Label(root, image=photo)
        img_label.image = photo  
        img_label.pack(pady=20)

        back_button = tk.Button(root, text="Back", command=home_page,
                                font=("Comic Sans MS", 20),
                                bg='darkblue',
                                fg='lightblue',
                                relief="raised",
                                borderwidth=2)
        back_button.pack(pady=20)
    
    def clear_screen():
        for widget in root.winfo_children():
            widget.destroy()
    
    root.mainloop()

home_page()
