import inflect

p = inflect.engine()


nameList = []
print("What are the names? ")
try:
    while True:
        names = input()
        nameList.append(names)
except EOFError:
    pass

output = p.join(nameList)
print(f"Adieu, adieu, to {output}")
