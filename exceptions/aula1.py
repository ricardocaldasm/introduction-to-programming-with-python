while True:
    try:
        x = int(input("Valor: "))
    except ValueError:  # exceptional
        pass
    else:
        break

print(f"O valor é {x}")

# pode ser usada também a função .isnumeric

a = "5"
print(a.isnumeric())  # somente utilizado caso 'a' seja string
