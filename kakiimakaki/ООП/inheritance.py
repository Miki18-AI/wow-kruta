from game_classes import Warrior, Mage
import random


class Archer(Warrior):
    def __init__(self, health=100, stamina=100,arrows=20):
        super().__init__(health, stamina)
        self.arrows = arrows
    def introduces(self):
        super().introduces()
        print('---------------')
        print(f'Arrows: {self.arrows}')
        print('---------------')
    def _critical_hit(self, target):
        target.health -=15
        print("---------------")
        print(f'{self.__class__.__name__} повезло и он стреляет критической атакой здоровье у {target.__class__.__name__} снижено до {target.health} ')
    def attacks(self,target):
        crit = random.randint(0, 100)
        if crit <= 50 and crit >= 0:
            self._critical_hit(target)
        else:
            super().attacks(target)
    def megaattacks(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} нападает')
        target.health -= 12
        self.arrows -= 3
        print(f'Здоровье у {target.__class__.__name__} снизилось до {target.health}')
        print(f'У {self.__class__.__name__} осталось {self.arrows} стрел')
        print("---------------")
class Alchemist(Mage):
    def __init__(self, health=100, mana=100,flasks=10):
        super().__init__(health, mana)
        self.flasks = flasks
    def introduces(self):
        super().introduces()
        print('---------------')
        print(f'Flasks: {self.flasks}')
        print('---------------')
    def attacks(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} использует бутыль с огнем против {target.__class__.__name__}, \nно при этом задевает себя')
        target.healt -= 10
        self.flasks -= 1
        print(f'Здоровье у {target.__class__.__name__} понижено до {target.healt}')
        print(f'Здоровье у {self.__class__.__name__} понижено до {self.healt}')
        print(f'У {self.__class__.__name__} осталось {self.flasks} алхимических бутылей')
        print("---------------")
    def heals(self, target):
        print("---------------")
        print(f'{self.__class__.__name__} применяет лечебное зелье')
        target.healt += 15
        self.flasks -= 1
        print(f'Здоровье у {target.__class__.__name__} повышено до {target.healt}',
              f'\nУ {self.__class__.__name__} осталось {self.flasks} бутылей')
        print("---------------")
unit1 = Archer()
unit2 = Alchemist()
unit1.attacks(unit2)
