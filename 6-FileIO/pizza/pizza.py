import sys
import csv
from tabulate import tabulate


if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif not (sys.argv[1]).endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1], "r") as file:
        menu = csv.DictReader(file, fieldnames=["Sicilian Pizza", "Small", "Large"])
        print(tabulate(menu, tablefmt="grid"))
except FileNotFoundError:
    print("not found")
    sys.exit
