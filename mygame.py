import tkinter as tk
from PIL import Image, ImageTk
import random
from pathlib import Path
from classes import Player, Weapon


class Game:
	def __init__(self) -> None:
		image_img_dir = Path(__file__).parent / 'img'
		self.window = tk.Tk()
		self.window.attributes('-fullscreen', True)
		self.window.bind('<Escape>', lambda _: self.window.destroy())
		self.font_size = min(self.window.winfo_screenwidth(), self.window.winfo_screenheight())

		self.wimdow.option_add('*Font', ('Impact',))

		self.image_size = self.window.winfo_screenwidth() // 3

		self.player = Player('Вася Питонов', 'Player.png', 1, 100, 0)
		self.enemy = Player('A-54', 'A-19.png', 1, 100, 0)

		self.player_frame = tk.Frame(self.window)
		self.player_frame.pack(side='left')
		image = Image.open(self.img_dir / self.player_image)
		image = image.rezize((self.image_size, self.image_size))
		image_tk = ImageTk.PhotoImage(image=image)
		tk.Label(self.player_frame, image=image_tk).pack()
		tk.Label(self.player_frame, text=f'Имя: {self.player.name}').pack()
		tk.Label(self.player_frame, text=f'Здоровье: {self.player.hp}').pack()
		tk.Label(self.player_frame, text=f'Уровень: {self.player.player.level}').pack()
		tk.Label(self.player_frame, text=f'Опыт: {self.player.xp}').pack()

		self.combat_frame = tk.Frame(self.window)
		self.combat_frame.pack(side='left')
		tk.Button(self.combat_frame, text='атака', command=atack())

		

		self.enemy_frame = tk.Frame(self.window)
		self.enemy_frame.pack(side='left')

		self.window.mainloop()
	
	def atack(self) -> None:
		self.player.hp -= 10


Game()
