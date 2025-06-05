class Warrior:
    def __init__(self, health=100, stamina=100):
        self.health = health
        self.stamina = stamina

    def __str__(self):
        s1 = '---------------\n'
        s2 = f'Class: {self.__class__.__name__}'
        s3 = f'\nHealth: {self.health}'
        s4 = f'\nStamina: {self.stamina}\n'
        s5 = '---------------'
        return s1 + s2 + s3 + s4 + s5

    def __add__(self, target):
        if isinstance(target, (Warrior, Mage)):
            print('---------------')
            print(f'{self.__class__.__name__} накладывает повязку из',
                f'целебных трав {target.__class__.__name__}')
            self.stamina -= 20
            target.health += 10
            print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}',
                f'\nУ {self.__class__.__name__} осталось {self.stamina} единиц запаса сил')
            print('---------------')
        elif isinstance(target, int):
            self.health += target
            print(f'Здоровье у {self.__class__.__name__} повышено на  {target} очков')
        elif isinstance(target, list):
            print(f'{self.__class__.__name__} присоединяется к отряду')
            target.append(self)

    def __sub__(self, target):
        if isinstance(target, (Warrior, Mage)):
            print('---------------')
            print(f'{self.__class__.__name__} наносит урон мечом {target.__class__.__name__}')
            target.health -= 3
            print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
            print('---------------')
        elif isinstance(target, int):
            self.health -= target
            print(f'Здоровье у {self.__class__.__name__} снижено на  {target} очков')
        elif isinstance(target, list):
            print(f'{self.__class__.__name__} уходит из отряда')
            target.remove(self)

    def __call__(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}'
              f'\nStamina: {self.stamina}')
        print('---------------')
    def __setattr__(self, attribute, value):
        if value > 100:
            self.__dict__[attribute] = 100
        elif value < 0:
            self.__dict__[attribute] = 0
        else:
            self.__dict__[attribute] = value
    def __len__(self):
        return len(self.__dict__)
class Mage:
    def __init__(self, health=60, mana=120):
        self.health = health
        self.mana = mana

    def __str__(self):
        s1 = '---------------\n'
        s2 = f'Class: {self.__class__.__name__}'
        s3 = f'\nHealth: {self.health}'
        s4 = f'\nStamina: {self.mana}\n'
        s5 = '---------------'
        return s1 + s2 + s3 + s4 + s5

    def __add__(self, target):
        if isinstance(target, (Warrior, Mage)):
            print('---------------')
            print(f'{self.__class__.__name__} накладывает заклинание ',
                f'лечения  {target.__class__.__name__}')
            self.mana -= 20
            target.health += 10
            print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}',
                f'\nУ {self.__class__.__name__} осталось {self.mana} единиц маны')
            print('---------------')
        elif isinstance(target, int):
            self.health += target
            print(f'Здоровье у {self.__class__.__name__} повышено на  {target} очков')
        elif isinstance(target, list):
            print(f'{self.__class__.__name__} присоединяется к отряду')
            target.append(self)

    def __sub__(self, target):
        if isinstance(target, (Warrior, Mage)):
            print('---------------')
            print(f'{self.__class__.__name__} наносит урон мечом {target.__class__.__name__}')
            target.health -= 3
            print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
            print('---------------')
        elif isinstance(target, int):
            self.health -= target
            print(f'Здоровье у {self.__class__.__name__} снижено на  {target} очков')
        elif isinstance(target, list):
            print(f'{self.__class__.__name__} уходит из отряда')
            target.remove(self)
    def __setattr__(self, attribute, value):
        if value > 100:
            self.__dict__[attribute] = 100
        elif value < 0:
            self.__dict__[attribute] = 0
        else:
            self.__dict__[attribute] = value
    def __len__(self):
        return len(self.__dict__)
unit1 = Warrior()
unit2 = Mage()
print(unit1)
t = []
unit1 - unit2
print(len(unit2))