import random


def main():
    userLevel = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(userLevel)
        answer = x + y
        try:
            userAnswer = int(input(f"{x} + {y} = "))
        except ValueError:
            userAnswer = None
            continue
        if userAnswer == answer:
            score += 1
            continue
        else:  
            for attempt in range(3):
                try:
                    print("EEE")
                    userAnswer = int(input(f"{x} + {y} = "))
                except ValueError:
                    userAnswer = None
                    continue
                if userAnswer == answer:
                    score += 1
                    break
                elif attempt < 2:
                    continue
                else:
                    print(f"Answer: {x} + {y} = {answer}")
                    continue
            else:
                continue
    print("Score:", score)


# output the user’s score


def get_level():
    while True:
        try:
            level = input("Level: ")
            level = int(level)
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        rando1 = random.randint(1, 9)
        rando2 = random.randint(1, 9)
        return rando1, rando2
    if level == 2:
        rando1 = random.randint(10, 99)
        rando2 = random.randint(10, 99)
        return rando1, rando2
    if level == 3:
        rando1 = random.randint(100, 999)
        rando2 = random.randint(100, 999)
        return rando1, rando2
    else:
        raise ValueError("Level range is invalid")


# returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:


if __name__ == "__main__":
    main()
