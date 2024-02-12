def main():
    meal = input("What's the time? ")
    hours, minutes = meal.split(":")
    convert(meal)

    """
    if 7 <= meal <= 8:
        print("breakfast time")
    elif 12 <= meal <= 13:
        print("lunch time")
    elif 18 <= meal <= 19:
        print("dinner time")
    """


def convert(time):
    time = int(minutes) / 30 + int(hours)


main()
