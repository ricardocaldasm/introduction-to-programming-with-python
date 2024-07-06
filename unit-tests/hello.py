def main():
    name = input("Qual seu nome? ")
    print(hello(name))


def hello(to="mundo"):
    return f"Olá, {to}"


if __name__ == "__main__":
    main()
