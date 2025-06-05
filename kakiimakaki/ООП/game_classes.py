class Warrior:
    def __init__(self, health=100, stamina=100):
        self.__health = health
        self.__stamine = stamina
    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, new_health):
        if self.__health > 100:
            self.__health = 100
        elif self.__health < 0:
            self.__health = new_health
    def introduces(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.healt}',
              f'\nStamina: {self.stamine}')
        print('---------------')
    def heals(self, target):
        print("---------------")
        print(f'{self.__class__.__name__} применяет лечебные травы')
        target.health += 10
        self.stamine -= 20
        print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}',
              f'\nУ {self.__class__.__name__} осталось {self.stamine} едениц магии')
        print("---------------")
    def attacks(self, target):
        print("---------------")
        print(f'{self.__class__.__name__} нападает на {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__} снизилось до {target.health}')
        print("---------------")
class Mage:
    def __init__(self, health=60, mana=100):
        self.health = health
        self.mana = mana
    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, new_health):
        if self.__health > 100:
            self.__health = 100
        elif self.__health < 0:
            self.__health = new_health
    def introduces(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.healt}',
              f'\nStamina: {self.mana}')
        print('---------------')
    def heals(self, target):
        print("---------------")
        print(f'{self.__class__.__name__} применяет заклинание лечения')
        target.healt += 10
        self.mana -= 20
        print(f'Здоровье у {target.__class__.__name__} повышено до {target.healt}',
              f'\nУ {self.__class__.__name__} осталось {self.mana} едениц магии')
        print("---------------")
    def attacks(self, target):
        print("---------------")
        print(f'{self.__class__.__name__} нападает')
        target.healt -= 3
        print(f'Здоровье у {target.__class__.__name__} снизилось до {target.healt}')
        print("---------------")