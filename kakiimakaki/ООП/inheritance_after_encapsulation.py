
from encapsulation import Warrior, Mage
import random



class Knight(Warrior):
    def __init__(self, health = 100, armor = 100, stamina=100):
        super().__init__(health,stamina)
        self.__armor = armor
    def _set_health(self, points):
        if points > 0:
            super()._set_health(points)
        elif points < 0:
            if self.__armor > abs(points):
                self.__armor += points
                print(f'Броня у {self.__class__.__name__} понижено до {self.__armor}')
            elif self.__armor <= abs(points) and self.__armor > 0:
                self.__armor == 0
                print("Броня уничтожена")
            elif self.__armor == 0:
                super()._set_health(points)
    def heals(self, target):
        if self.__stamine >= 20:
            print("---------------")
            print(f'{self.__class__.__name__} применяет лечебные травы')
            target._set_health(+10)
            self.__stamine -= 20
            print(f'Здоровье у {target.__class__.__name__} повышено до {target._get_health()}',
                f'\nУ {self.__class__.__name__} осталось {self.__stamine} едениц стаимыны')

    def __critical_hit(self,target):
        target._set_health(-10)
        print("---------------")
        print(f'{self.__class__.__name__} повезло и он бъет критическим уроном здоровье у {target.__class__.__name__} снижено до {target._get_health()} ')

    def attacks(self, target):
        crit = random.randint(0,100)
        if crit <= 30 and crit >= 0:
            self.__critical_hit(target)
        else:
            super().attacks(target)

class Wizard(Mage):
    def __init__(self, health = 100, barrier = 100, mana=100):
        super().__init__(health,mana)
        self.__barrier = barrier
    def _set_health(self, points):
        if points > 0:
            super()._set_health(points)
        elif points < 0:
            if self.__barrier > abs(points):
                self.__barrier += points
                print(f',барьер у {self.__class__.__name__} понижено до {self.__barrier}')
            elif self.__barrier <= abs(points) and self.__barrier > 0:
                self.__barrier == 0
                print("барьер уничтожена")
            elif self.__barrier == 0:
                super()._set_health(points)
    def fireball(self,target):
        target._set_health(-15)
        print("---------------")
        print(f'{self.__class__.__name__} повезло и он бъет фаер боллом здоровье у {target.__class__.__name__} снижено до {target._get_health()} ')


    def attacks(self, target):
        crit = random.randint(0,100)
        if crit <= 20 and crit >= 0:
            self.fireball(target)
        else:
            super().attacks(target)

