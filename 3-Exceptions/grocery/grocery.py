# prompts the user for items, one per line, until the user inputs control-d
# store items in a list
# output the user’s grocery list in all uppercase
# sorted alphabetically by item
# prefixing each line with the number of times the user inputted that item

grocerylist = {}

print("What are your items? ")
try:
    while True:
        items = input().strip().upper()
        if items in grocerylist:
            grocerylist[items] += 1
        else:
            grocerylist[items] = 1
except EOFError:
    pass

for i, c in sorted(grocerylist.items()):
    print(f"{c} {i}")
