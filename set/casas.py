estudantes = [
    {"name":"Hermione", "casa":"Grinfinória"},
    {"nome":"Herry", "casa":"Grinfinória"},
    {"nome":"Draco", "casa":"Sonserina"},
    {"nome":"Padma", "casa":"Corvinal"},
]

casas = set()
for estudante in estudantes:
    casas.add(estudante["casa"])

for casa in sorted(casas):
    print(casa)