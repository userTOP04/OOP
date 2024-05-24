import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk


class Game:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.combat_messages = tk.Listbox(self.window)
        self.combat_messages.insert(0, 'Вася')
        self.combat_messages.insert(tk.END, 'ася')
        self.combat_messages.insert(tk.END, 'ся')
        self.combat_messages.pack()
        self.image_hero = Path(__file__).parent / 'img' / 'Vasia.png'
        self.image_enemy = Path(__file__).parent / 'img' / 'Enemy.png'
        self.img1 = Image.open(self.image_hero)
        self.photo1 = ImageTk.PhotoImage(self.img1)
        self.label1 = tk.Label(self.window, image=self.photo1)
        self.label1.pack()
        tk.PhotoImage()
        self.window.mainloop()



Game()