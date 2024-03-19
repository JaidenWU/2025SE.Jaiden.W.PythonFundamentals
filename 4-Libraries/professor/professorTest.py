import random


def main():
    correct = 0
    incorrect = 0
    attempts = 0

    def get_level():
        while True:
            try:
                level = int(input("Level: "))
                if level < 1 or level > 3:
                    continue
                else:
                    return level
            except ValueError:
                continue

    def generate_integer(level):
        nonlocal correct, incorrect, attempts  # Adds the variables from the outside in

        while True:
            for _ in range(10):
                x = random.randint(1, 9)
                y = random.randint(1, 9)

                answer = x + y

                for _ in range(3):
                    prompt = int(input(f"What's the answer to {x} + {y}: "))
                    if prompt == answer:
                        correct += 1
                        break
                    else:
                        attempts += 1
                        incorrect += 1
                        print("EEE")
                print(f"{x} + {y} = {answer}")
            break

    level = get_level()  # Added line to get the level
    generate_integer(level)  # Added line to call generate_integer() with the level

    total = 10 - incorrect
    print(f"You got : {total}/10")


if __name__ == "__main__":
    main()