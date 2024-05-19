import random


class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("harry")


@property
def house(self):
    return self._house


@house.setter
def house(self, house):
    if house not in ["shit", "fuck"]:
        raise ValueError("invalid house")
    self._house = house


def get_student():
    name = input("name: ")
    house = input("house: ")
    return Student(name, house)
