name = input("Qual o seu nome? ")

"""
file = open(r"file-io\names.txt", "a") #"a" para append
file.write(f"{name}\n")
file.close()
"""

with open(r"file-io\names.txt", "a") as file: #neste caso, o file.close() não é necessário pois o arquivo é fechado após a função
    file.write(f"{name}\n")

with open(r"file-io\names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Olá,", line.rstrip()) #rstrip() remove a implementação da \n para leitura de novas linhas no print

with open(r"file-io\names.txt", "r") as file:
    for line in file:
        print("Olá,", line.rstrip())