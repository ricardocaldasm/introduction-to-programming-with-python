students = list()

with open(r"file-io\students.csv") as file:
    for line in file:
        name, year = line.rstrip().split(",")
        student = {"name":name, "year":year}


for student in students:
    print(f"{student["name"]} nasceu em {student["year"]}")


"""
student["name"] = name
student["year"] = year
students.append(student)
"""