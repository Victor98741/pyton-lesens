from random import randint
h = 0


class Potion:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality

    def __str__(self):
        return f'this potion named: {self.name}'

    def get_quality(self):
        return self.quality

    def get_name(self):
        return self.name

    def __add__(self, other):
        d1 = len(self.name) // 2
        d2 = len(other.name) // 2
        summ = self.name[:d1] + other.name[d2:]
        sr = (self.quality + other.quality) // 2
        return Potion(summ, sr)

    def __sub__(self, other):

        d1 = len(self.name) // 2
        d2 = len(other.name) // 2
        summ = self.name[:d1] + other.name[d2:]
        x = self.quality
        y = other.quality
        if (int(x) > int(y)):
            h = int(x) - int(y)
        else:
            h = int(y) - int(x)
        return Potion(summ, int(h))

    def print_quality(self):
        if self.quality > 75:
            print('Potion is very good')
        elif self.quality > 50:
            print('Potion is average')
        else:
            print('Potion has bad quality')


class QuolityPotion(Potion):
    def special(self):
        return QuolityPotion(self.name, self.quality + 20)


class NotQuolityPotion(Potion):
    def special(self):
        return NotQuolityPotion(self.name, self.quality - 20)


quolity = randint(1, 100)
qPotion = QuolityPotion('Veritaserum', quolity)
game = True
potions = {}
while game:
    potion = input(f'What potion do you want to make? q - for quality, n - for not quality').lower()
    if potion == "exit":
        game = False
    else:
        potion_name = input('enter potion name: ')
        potion_quality = randint(1, 100)
        if potion == 'q':
            new_potion = QuolityPotion(potion_name, potion_quality)
        else:
            new_potion = NotQuolityPotion(potion_name, potion_quality)
        potions[potion_name] = new_potion
        if len(potions) >= 2:
            action = input(f' Add(+) or Subtract(-) your potions? ').lower()
            potion1 = potions.popitem()[1]
            potion2 = potions.popitem()[1]
            if action == '+':
                mixed_potion = potion1 + potion2
            else:
                mixed_potion = potion1 - potion2
                
            print('Start mixin potions...')
            if mixed_potion.get_quality() < 30:
                print('Kaboom! Potion exploded')
                game = False
            else:
                potions[mixed_potion.get_name()] = mixed_potion
                print(f'Your potion name: {mixed_potion.get_name()}')
                print(f'Potion quality: {mixed_potion.get_name()}, Be careful next time')

print(qPotion)
