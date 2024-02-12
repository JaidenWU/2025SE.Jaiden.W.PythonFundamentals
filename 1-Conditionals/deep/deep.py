def main():
    answer = input(
        "What's the Great Question of Life, the Universe and Everything? "
    ).casefold()
    match answer:
        case "42" | "forty two" | "forty-two":
            print("Yes")
        case _:
            print("No")


main()
