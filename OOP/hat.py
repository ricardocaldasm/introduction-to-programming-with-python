import random


class Hat:
    #def __init__(self):
    houses = ["Vermelho", "Verde", "Amarelo", "Azul"]

    @classmethod
    def sort(cls, name): #era self
        print(name, "is in", random.choice(cls.houses)) #era self


#hat = Hat()
Hat.sort("Harry")
