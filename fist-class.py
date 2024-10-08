class Piople:
    def __init__(self, name):
        self.name = name
        self.counteys = 2
    def subskrite(self, name_people):
        print(f'{self.name} подписался на {name_people}')
Pit = Piople("Pit")
Vasya = Piople("Vasya")
print(Pit)
print(Pit.__dict__)
Pit.tatu = "yes"
print(Pit.__dict__)
Pit.subskrite("Федя")