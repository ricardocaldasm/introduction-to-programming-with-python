names = list()

# cria uma lista para adicionar todas as linhas do arquivo txt em diferentes posições
with open(r"file-io\names.txt") as file:  # o padrão já é "r" para read, não é necessário especificar
    for line in file:
        names.append(line.rstrip())

# mostra a lista em ordem alfabética
for name in sorted(names):
    print(f"Olá, {name}")
