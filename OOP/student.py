class Student:
    def __init__(self, name, house):  # method - Adicionando variáveis a objetos
        if not name:
            raise ValueError("Missing name.")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house.")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}.")


def get_student():
    """
    student = Student()
    student.name = input("Name: ") -> object
    student.house = input("House: ") -> object
    """
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)  # name, house -> objects


if __name__ == "__main__":
    main()
