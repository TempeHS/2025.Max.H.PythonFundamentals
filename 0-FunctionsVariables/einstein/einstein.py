def einstein_calculation(mass):
    speed_of_light = 300000000
    energy = mass * speed_of_light**2
    return energy


def main():
    mass = int(input("enter a mass "))
    energy = einstein_calculation(mass)
    print("energy in joules", energy)


if __name__ == "__main__":

    main()
