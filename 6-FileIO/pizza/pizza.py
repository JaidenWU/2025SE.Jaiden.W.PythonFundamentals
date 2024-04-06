import sys
import csv
from tabulate import tabulate

menu = []

# exceptions
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
prompt = sys.argv[1]
if not prompt.endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(prompt) as file:
        reader = csv.reader(file)
        for row in reader:
            menu.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")


print(tabulate(menu, headers="firstrow", tablefmt="grid"))
