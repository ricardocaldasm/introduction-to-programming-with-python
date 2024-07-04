# quando usamos o ',' python coloca um espaço automaticamente
print("Olá" + "Mundo")
print("Olá", "Mundo")
# padrão: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# flush força que o resultado apareça imediatamente, mesmo sem linha nova. ex: uso do time.sleep e print('.', end='')
nome = str(input("Nome completo: "))
# pnome, snome = nome.split(" ") somente para dois nomes
lista = list()
lista = nome.split(" ")
print(f"Nome: {lista}")

print(f"{1000:,}")  # separador com ','

# função potência: pow(2,3) ou 2**3
