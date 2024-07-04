from random import choice, shuffle
from statistics import mean
from sys import argv

moeda = choice(["cara", "coroa"])
print(moeda)

lista = ["a", "b", "c", "d", "e"]
shuffle(lista)
print(lista)

print(mean([1,2]))

print(argv[0])