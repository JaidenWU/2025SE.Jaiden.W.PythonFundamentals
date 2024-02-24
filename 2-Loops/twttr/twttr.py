def main():
    text = input("Type your tweet: ")
    vowel = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    for letter in text:
        if letter in vowel:
            print("", sep="", end="")
        else:
            print(letter, sep="", end="")
    print()


main()
