# Цель: закрепить знания множественного наследования в Python.
# Задача "Мифическое наследование"

# 1 Вариант******************************************

class Horse:

    def __init__(self):
        super().__init__()
        self.x_distance = 0  # пройденный путь sound = 'Frrr'
        self.sound = 'Frrr'  # звук, который издаёт лошадь

    def run(self, dx):  # где dx-изменение дистанции, увеличивает x_distance на dx
        self.x_distance += dx


class Eagle:
    def __init__(self):
        super().__init__()
        self.y_distance = 0  # высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл(отсылка)

    def fly(self, dy):  # где dy-изменение дистанции, увеличивает y_distance на dy
        self.y_distance += dy
        #return self.y_distance


class Pegasus(Horse, Eagle):
    # def __init__(self):
    #     Horse.__init__(self)
    #     Eagle.__init__(self)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(f'{self.sound}')

# В первом варианте выводится звук Frrr вместо I train, eat, sleep, and repeat. Чтобы получить звук как в ответе
# задания необходимо в Pegasus поменять порядок наследования Pegasus(Eagle, Horse) или его явно определять
# через init в Pegasus



print(Pegasus.mro())

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

# 2 Вариант ******************************************
class Horse:

    def __init__(self):
        #super().__init__()
        self.x_distance = 0  # пройденный путь sound = 'Frrr'
        self.sound = 'Frrr'  # звук, который издаёт лошадь

    def run(self, dx):  # где dx-изменение дистанции, увеличивает x_distance на dx
        self.x_distance += dx


class Eagle:
    def __init__(self):
        #super().__init__()
        self.y_distance = 0  # высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл(отсылка)

    def fly(self, dy):  # где dy-изменение дистанции, увеличивает y_distance на dy
        self.y_distance += dy
        #return self.y_distance


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(f'{self.sound}')


print(Pegasus.mro())

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
