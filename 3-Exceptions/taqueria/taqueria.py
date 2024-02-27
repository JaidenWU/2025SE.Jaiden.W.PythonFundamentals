menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

print("What do you want to order: ")

# create empty list to add the ordered items
items_ordered = []

try:
    while True:
        item = input().strip().title()
        if item in menu:
            # adds item to our items_ordered list
            items_ordered.append(item)
            # adds up all the item in items_ordered
            cost = sum(menu[item] for item in items_ordered)
            # adds dollar sign and rounds to 2 decimal places
            print(f"Total: ${cost:.2f}")
        else:
            print("not on the menu, try again")
except EOFError:
    pass
