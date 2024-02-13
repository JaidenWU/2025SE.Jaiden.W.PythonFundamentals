def main():
    meal = input("What's the time? ")
    meal = convert(meal)
    if 7 <= meal <= 8:
        print("breakfast time")
    elif 12 <= meal <= 13:
        print("lunch time")
    elif 18 <= meal <= 19:
        print("dinner time")
    else:
        print("nothing")


def convert(time):
    hours, minutes = time.split(":")
    time = float(hours) + float(minutes) / 60
    return time


main()
