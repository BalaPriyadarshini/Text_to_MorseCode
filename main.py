import tkinter as tk
from PIL import Image, ImageTk

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


class TextToMorse:

    def __init__(self, root):
        self.root = root
        self.root.title("Text To Morse Code Converter")
        self.root.geometry("800x500")
        self.opening_screen()

    def opening_screen(self):
        self.image_path = r"background image path"
        self.image = Image.open(self.image_path)
        self.bg_image = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(root, image=self.bg_image)
        self.label.place(x=0, y=0, relwidth=1, relheight=1)
        tk.Label(self.root, text="Text:", bg="gray13", fg="green2", font=('Helvetica', 14, 'italic')).place(x=230, y=150)
        self.text_entry = tk.Entry(self.root, bg="gray5", fg="green2", insertbackground="green", font=('Helvetica', 14))
        self.text_entry.place(x=400, y=150)
        tk.Label(self.root, text="Morse", bg="gray14", fg="green2", font=('Helvetica', 14, 'italic')).place(x=230, y=250)
        tk.Label(self.root, text="Code:", bg="gray15", fg="green2", font=('Helvetica', 14, 'italic')).place(x=290, y=250)
        self.morse_box = tk.Text(self.root, bg="gray5", fg="green2", height=5, width=30, font=('Helvetica', 14))
        self.morse_box.place(x=400, y=250)
        tk.Button(self.root, text="Convert", command=self.convert, bg="gray7", fg="green2", font=('Helvetica', 12, 'bold')).place(x=660, y=150)

    def convert(self):
        self.morse_box.delete('1.0', tk.END)
        msg = self.text_entry.get().upper()
        converted_msg = ''
        for ch in msg:
            if ch != " ":
                converted_msg += MORSE_CODE_DICT[ch] + ' '
            else:
                converted_msg += '  '
        self.morse_box.insert(tk.END, converted_msg)


if __name__ == "__main__":
    root = tk.Tk()
    TextToMorse(root)
    root.mainloop()
