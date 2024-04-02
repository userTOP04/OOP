"""
ООП - стиль прогрпмирования
Класс - фабрика экземпляров
Экземпляр - конкретная реализация объекта
"""


class Player:
    # Класс это переменные + функции
    def __init__(self, name: str, hp: int) -> None:
        '''
        Конструктор класс
        Вызывается сам после создания эгземпляра
        self - ссылка на сам экземпляр
        Все атрибуты определяются тут!!! 
        '''
        self.hp = hp  # экземплярный атребут
        self.name = name
        self.attack_power = 1

    def show(self) -> None:
        print(self.name)
        print(self.hp)

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


class Game:
    def __init__(self) -> None:
        self.player = Player('Gigachad:', -100) # Создание экземпляра класса Player
        self.player.heal(200)  # Gigachad выпил растишки под фонг
        self.enemy = Player('Lox:', 100)
        self.player.show()
        self.enemy.show()
        self.is_running = False
        self.fight()

    def fight(self) -> None:
        self.is_running = True
        while self.is_running:
            self.player.show()
            self.player.attacck(self.enemy)
            self.enemy.show()
            self.player.attacck(self.enemy)



Game()



