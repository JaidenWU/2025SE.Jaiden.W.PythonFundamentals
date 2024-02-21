def rps_logic():
    player_choice = input("Rock, Paper or Scissor ")
    player_choice = player_choice.lower()
    computer_choice = generate_random()
    match player_choice:
        case "rock":
            match computer_choice:
                case "rock":
                    print("Tie")
                case "paper":
                    print("Loss")
                case "scissor":
                    print("Won")

        case "paper":
            match computer_choice:
                case "rock":
                    print("Won")
                case "paper":
                    print("Tie")
                case "scissor":
                    print("Loss")

        case "scissor":
            match computer_choice:
                case "rock":
                    print("Loss")
                case "paper":
                    print("Won")
                case "scissor":
                    print("Tie")
        case _:
            print("type Rock Paper Scissor pretty please ")


def generate_random():
    return "paper"


rps_logic()
