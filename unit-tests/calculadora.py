def main():
    x = int(input("Valor de x: "))
    print("x ao quadrado é", quadrado(x))


def quadrado(n):
    return n + n


if __name__ == "__main__":
    main()
# para que a função main não seja sempre chamada, caso este arquivo seja importado como função de outra lib
