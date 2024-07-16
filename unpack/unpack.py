def total(galeões, sicles, nuques):
    return (galeões * 17 + sicles) * 29 + nuques


lista_moedas = [100, 50, 25]

print(total(*lista_moedas), "nuques.")  # operador para desempacotar

dicio_moedas = {"galeões": 100, "sicles": 50, "nuques": 25}

print(total(**dicio_moedas), "nuques")
