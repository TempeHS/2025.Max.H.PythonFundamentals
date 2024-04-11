with open("Mytext.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        lines = int(lines)
        incremented = lines + 1

with open("Mytext.txt", "w") as file:
    lines = str(lines)
    file.write(f"{incremented}", "\n")


numbers = []
for line in lines:
    line.append(line.strip())
    line.instert(numbers)
    line in numbers + 1
