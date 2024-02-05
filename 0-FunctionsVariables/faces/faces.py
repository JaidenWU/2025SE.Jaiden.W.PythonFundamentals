def main():
    emoji = input("How is your day going? ")
    convert(emoji)


def convert(to):
    print(to.replace(":)", "🙂").replace(":(", "🙁"))


main()
