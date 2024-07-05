from random import choice, shuffle
from statistics import mean
from sys import argv

moeda = choice(["cara", "coroa"])
print(moeda)

lista = ["a", "b", "c", "d", "e"]
shuffle(lista)
print(lista)

print(mean([1, 2]))

if len(argv) < 2:
    exit("Poucos termos")
'''
elif len(argv) > 2:
    exit("Muitos termos")

print("Olá, meu nome é", argv[1])  # digitar no prompt libraries\aula1.py Ricardo
'''
for arg in argv[1:]:
    print("Olá, meu nome é", arg)