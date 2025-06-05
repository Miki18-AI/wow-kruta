class Warrior:
    def __init__(self, health=100, stamina=100):
        self.__health = health
        self.__stamine = stamina
    def _get_health(self):
        return self.__health
    def _set_health(self, points):
        self.__health += points
        if self.__health > 100:
            self.__health = 100
        elif self.__health < 0:
            self.__health = 0
    def introduces(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.__health}',
              f'\nStamina: {self.__stamine}')
        print('---------------')
    def heals(self, target):
        if self.__stamine >= 20:
            print("---------------")
            print(f'{self.__class__.__name__} применяет лечебные травы')
            target._set_health(+10)
            self.__stamine -= 20
            print(f'Здоровье у {target.__class__.__name__} повышено до {target._get_health()}',
                f'\nУ {self.__class__.__name__} осталось {self.__stamine} едениц стаимыны')
        else:
            print("Недостаточно сил для использования этой способности.")
        print("---------------")
    def attacks(self, target):
        if target._get_health() > 3:
            print("---------------")
            print(f'{self.__class__.__name__} нападает на {target.__class__.__name__}')
            target._set_health(-3)
            print(f'Здоровье у {target.__class__.__name__} снизилось до {target._get_health()}')
            print("---------------")
        elif target._get_health() <= 3:
            print(f'{self.__class__.__name__} наносит последний удар и побеждает {target.__class__.__name__}\n {target.__class__.__name__} покидает отряд лузер')
        else:
            print("Персонаж уже умер.")
class Mage:
    def __init__(self, health=60, mana=100):
        self.__health = health
        self.__mana = mana
    def _get_health(self):
        return self.__health
    def _set_health(self, points):
        self.__health += points
        if self.__health > 100:
            self.__health = 100
        elif self.__health < 0:
            self.__health = 0
    def introduces(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.__health}',
              f'\nStamina: {self.__mana}')
        print('---------------')
    def heals(self, target):
        if self.__mana >= 20:
            print("---------------")
            print(f'{self.__class__.__name__} применяет заклинание лечения')
            target._set_health (+10)
            self.__mana -= 20
            print(f'Здоровье у {target.__class__.__name__} повышено до {target._get_health()}',
                f'\nУ {self.__class__.__name__} осталось {self.__mana} едениц магии')
            print("---------------")
        else:
            print("Недостаточно маны для использования этой способности.")
    def attacks(self, target):
        if target._get_health() > 3:
            print("---------------")
            print(f'{self.__class__.__name__} нападает')
            target._set_health (-3)
            print(f'Здоровье у {target.__class__.__name__} снизилось до {target._get_health()}')
            print("---------------")
        elif target._get_health() <= 3:
            print(f'{self.__class__.__name__} наносит последний удар и побеждает {target.__class__.__name__}\n {target.__class__.__name__} покидает отряд лузер')
        else:
            print("Герой уже умер.")

