"""
ООП - стиль прогрпмирования
Класс - фабрика экземпляров
Экземпляр - конкретная реализация объекта
"""


class Player:
    # Класс это переменные + функции
    def __init__(self, name: str, hp: int, weapon=None) -> None:
        '''
        Конструктор класс
        Вызывается сам после создания эгземпляра
        self - ссылка на сам экземпляр
        Все атрибуты определяются тут!!! 
        '''
        self.hp = hp  # экземплярный атребут
        self.name = name
        self.attack_power = 1
        if weapon:
            self.weapon = weapon
        else:
            self.weapon = Weapon('Кулак', 1)
        

    def show(self) -> None:
        print(self.name)
        print('Жизни: ', self.hp)

    def heal(self, ammount: int) -> None:
        self.hp += ammount

    def attacck(self, enemy):
        if self.hp <= 0:
            return
        enemy.hp -= self.attack_power
        print(
            self.name,
            'атаковал',
            enemy.name,
            'на',
            self.attack_power
        )


class Weapon():
    def __init__(self, name: str, weapon_power: str) -> None:
        self.name = name 
        self.weapon_power = weapon_power
            



class Game:
    def __init__(self) -> None:
        self.player = Player('Gigachad:', -100, Weapon('Револьвер' 35)) # Создание экземпляра класса Player
        self.player.heal(200)  # Gigachad выпил растишки под фонг
        self.enemy = Player('Lox:', 100, )
        self.player.show()
        self.enemy.show()
        self.weapon1 = Weapon(self.player)
        self.is_running = True
        self.fight()

    def fight(self) -> None:
        self.is_running = True
        while self.is_running:
            self.player.attacck(self.enemy)
            self.player.show()
            self.check_winner()
            self.player.attacck(self.player)
            self.enemy.show()
            self.check_winner()
            

    def check_winner(self):
        if self.player.hp <= 0:
            print(self.player.name, 'победил')
            self.is_running = False
        elif self.enemy.hp <= 0:
            print(self.player.name, 'победил')
            self.is_running = False
        



Game()



