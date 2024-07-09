import re

name = input("Qual seu nome? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name): #junta as linhas de assign e if
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"Olá, {name}")
