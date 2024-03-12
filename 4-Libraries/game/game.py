import random


while True:
    try:
        level = input("Level: ")
        level = int(level)
        if level > 0:
            break
    except ValueError:
        pass

random = random.randint(1, level)

while True:
    try:
        userGuess = input("Guess: ")
        userGuess = int(userGuess)
        if userGuess < 0:
            continue
        elif userGuess < random:
            print("Too small!")
            continue
        elif userGuess > random:
            print("Too large!")
            continue
        elif userGuess == random:
            print("Just right!")
            break
    except ValueError:
        pass
