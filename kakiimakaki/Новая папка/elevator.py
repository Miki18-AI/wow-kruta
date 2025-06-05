class Elevator:
    def __init__(self,it=1, min=1,max=15):
        self.min = min
        self.max = max
        self.it = it
    def Up(self):
        if self.it <  self.max:
            self.it += 1
            print(f'Лифт поднимаеться на {self.it} этаж')
        else:
            print("Лифт не может поднятся выше")
    def Down(self):
        if self.it > self.min:
            self.it -= 1
            print(f'Лифт опускатся на {self.it} этаж')
        elif self.it > self.max or self.it < self.min:
            print("Неправильный номер этажа")
        else:
            print("Лифт не может опустится ниже")
l1 = Elevator()
l1.Down()
