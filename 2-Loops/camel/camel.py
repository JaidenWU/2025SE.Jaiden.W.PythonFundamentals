def main():
    # prompts user for name of variable
    var = input("What's the name of the variable? ")
    var = convert(var)


def convert(to):

    # search each letter to see if its uppercase
    for letter in to:
        if letter.isupper():
            print("_" + letter.lower(), end="")
        else:
            print(letter, end="")


main()
print()
