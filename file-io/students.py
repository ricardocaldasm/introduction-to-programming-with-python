with open(r"file-io\students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        # row se torna uma lista com os valores separados pela ","
        # rstrip() para retirar o \n implícito do arquivo .csv
        print(f"{row[0]} nasceu em {row[1]}")

with open(r"file-io\students.csv") as file:
    for line in file:
        name, year = line.rstrip().split(",")
        print(f"{name} nasceu em {year}")

students = list()

with open(r"file-io\students.csv") as file:
    for line in file:
        name, year = line.rstrip().split(",")
        student = {"name": name, "year": year}
        students.append(student)

"""
student["name"] = name
student["year"] = year
students.append(student)
"""

def get_name(student):
    return student["name"]

def get_year(student):
    return student["year"]

# for student in sorted(students, key = get_year): # por que não usa get_year()? Para que o key possa chamar todos os dicionários da lista
for student in sorted(students, key=lambda student:student["name"]): # equivalente à função get_name - lambda: função sem nome
    print(f"{student["name"]} nasceu em {student["year"]}")



