from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Urdu Alphabet Learning and Quiz")
root.geometry("600x500")
root.configure(bg='lightblue')

urdu_alphabet = [
    ('ا', 'Alif'), ('ب', 'Bay'), ('پ', 'Pay'), ('ت', 'Tay'), ('ٹ', 'Ttay'),
    ('ث', 'Ssay'), ('ج', 'Jeem'), ('چ', 'Chay'), ('ح', 'Hay'), ('خ', 'Khay'),
    ('د', 'Dal'), ('ڈ', 'Ddal'), ('ذ', 'Zal'), ('ر', 'Ray'), ('ڑ', 'Rray'),
    ('ز', 'Zay'), ('ژ', 'Zhay'), ('س', 'Seen'), ('ش', 'Sheen'), ('ص', 'Suaad'),
    ('ض', 'Zuad'), ('ط', 'Tua'), ('ظ', 'Zua'), ('ع', 'Ain'), ('غ', 'Ghain'),
    ('ف', 'Fay'), ('ق', 'Qaaf'), ('ک', 'Kaaf'), ('گ', 'Gaaf'), ('ل', 'Laam'),
    ('م', 'Meem'), ('ن', 'Noon'), ('ں', 'Noonghunna'), ('و', 'Wao'), ('ہ', 'Hay'),
    ('ء', 'Hamza'), ('ی', 'Yay'), ('ے', 'BarriYay')
]

quiz_questions = [
    ('ا', 'Alif', 'radio'), ('ب', 'Bay', 'entry'), ('پ', 'Pay', 'radio'), ('ت', 'Tay', 'entry'),
    ('ٹ', 'Ttay', 'radio'), ('ث', 'Ssay', 'entry'), ('ج', 'Jeem', 'radio'), ('چ', 'Chay', 'entry'),
    ('ح', 'Hay', 'radio'), ('خ', 'Khay', 'entry')
]



root.mainloop()
