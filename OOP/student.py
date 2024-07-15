class Student:
    def __init__(
        self, name, house, patronus
    ):  # method - Adicionando variáveis a objetos
        if not name:
            raise ValueError("Missing name.")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house.")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "Stag"
            case "Otter":
                return "Otter"
            case "Dog":
                return "Dog"
            case _:
                return "Wand"


def main():
    student = get_student()
    print("Expecto Patronum!")
    # print(f"{student.name} from {student.house}.")


def get_student():
    """
    student = Student()
    student.name = input("Name: ") -> object
    student.house = input("House: ") -> object
    """
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)  # name, house -> objects


if __name__ == "__main__":
    main()
