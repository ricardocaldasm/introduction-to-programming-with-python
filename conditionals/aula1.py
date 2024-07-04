def main():
    x = int(input("Valor: "))
    if par(x):
        print("Par")
    else:
        print("Ímpar")


def par(n):
    return n % 2 == 0  # em caso de condição, a função retorna um valor booleano.


main()

nome = str(input("Digite o nome: "))

match nome:
    case "Harry" | "Hermione" | "Ron":
        print("Grinfinória")
    case "Draco":
        print("Sonserina")
    case _:
        print("Quem?")
