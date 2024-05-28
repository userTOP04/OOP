import tkinter as tk
import random
from pathlib import Path
from PIL import Image, ImageTk


class Game:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)
        self.window.bind('<d>', lambda _: self.window.destroy())
        self.player = Player('Vasia Pythonov')
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack()
        combat_messages = tk.Listbox(self.main_frame)
        combat_messages.insert(0, 'Вася')
        combat_messages.insert(tk.END, 'A-54')
        combat_messages.pack()
        self.create_hero_screen()
        self.create_enemy_screen()
        self.window.mainloop()


    def create_hero_screen(self) -> None:
        hero_frame = tk.Frame(self.window)
        hero_frame.pack(side='left')
        image_hero = Path(__file__).parent / 'img' / 'Player.png'
        img_hero = Image.open(image_hero)
        image_widht = self.window.winfo_screenwidth() // 3
        aspect_ratio = img_hero.height / img_hero.width
        image_height = int(image_widht * aspect_ratio)
        img_hero = img_hero.resize((image_widht, image_height), Image.LANCZOS)
        self.photo_hero = ImageTk.PhotoImage(img_hero)
        tk.Label(hero_frame, image=self.photo_hero).pack()
        tk.Label(hero_frame, text=f'Имя: {self.player.player_name}').pack()
        tk.Label(hero_frame, text=f'Здоровье: {self.player.player_hp}').pack()

    def create_enemy_screen(self) -> None:
        enemy_frame = tk.Frame(self.window)
        enemy_frame.pack(side='right')
        image_enemy = Path(__file__).parent / 'img' / 'A-19.png'
        img_enemy = Image.open(image_enemy)
        image_widht = self.window.winfo_screenwidth() // 3
        aspect_ratio = img_enemy.height / img_enemy.width
        image_height = int(image_widht * aspect_ratio)
        img_enemy = img_enemy.resize((image_widht, image_height), Image.LANCZOS)
        self.photo_enemy = ImageTk.PhotoImage(img_enemy)
        tk.Label(enemy_frame, image=self.photo_enemy).pack()

class Player:
    def __init__(self, player_name) -> None:
        self.player_name = player_name
        self.player_hp = 100
        self.player_damage = random.randint(5, 10)

Game()