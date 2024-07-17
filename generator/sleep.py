def main():
    n = int(input("Valor de n: "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐑" * i  # vai gerando a medida que o programa roda (para números grandes)


if __name__ == "__main__":
    main()
