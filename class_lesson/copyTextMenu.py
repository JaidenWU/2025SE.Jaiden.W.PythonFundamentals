def main():
    while True:
        display_menu()
        user_choice = input("What would you like? ")
        if selection(user_choice):
            break


def display_menu():
    print("1) Selection 1")
    print("2) Selection 2")
    print("3) Selection 3")
    print("4) Selection 4")


def selection(user):
    if user == "1":
        selection_1()
    elif user == "2":
        selection_2()
    elif user == "3":
        selection_3()
    elif user == "4":
        return True
    else:
        print("Invalid Option")


def selection_1():
    print("Anything Else?")


def selection_2():
    print("Anything Else?")


def selection_3():
    print("Anything Else?")


main()
