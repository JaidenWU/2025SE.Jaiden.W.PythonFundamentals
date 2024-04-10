import sys
import csv

list = []

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif not (sys.argv[1]).endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                Last, First = row["name"].split(",")
                writer.writerow({"first": First, "last": Last, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
