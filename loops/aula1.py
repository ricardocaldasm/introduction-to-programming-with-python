for _ in range(3): #não é necessário (0,3) e não é necessário ter a variável caso você não a use
    print("Olá, mundo!")

while True:
    n = int(input("Valor: "))
    if n < 0:
        continue
    else:
        break

lista = [None, 3, 4] #None é a ausência de valor. Não é utilizado ""
print(lista[0])