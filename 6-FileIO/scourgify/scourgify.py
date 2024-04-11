import sys
import csv

if len(sys.argv) > 3:
    print("too many arguments")
    sys.exit
elif len(sys.argv) < 3:
    print("too few arguments")
    sys.exit
elif not (sys.argv[1]).endswith(".csv"):
    print("invalid input")
    sys.exit
else:
    print("you didnt do anything correct")
    sys.exit

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            with open(sys.argv[2], "w") as file2:
                writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for line in reader:
                    line["first"] = line.pop("name")
                    last, first = line["first"].split(", ")
                    line["first"] = first
                    line["last"] = last
                    writer.writerow(line)
    except:
        FileNotFoundError
    print("file not found")
    sys.exit
