import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

fonts = figlet.getFonts()


if len(sys.argv) == 1:
    prompt = input("Your text here: ")
    ran = random.choice(fonts)
    figlet.setFont(font=ran)
    print(figlet.renderText(prompt))

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        print("Invalid Usage")
        sys.exit()
    else:
        userfont = sys.argv[2]
        if userfont in fonts:
            prompt = input("Your text here: ")
            figlet.setFont(font=userfont)
            print(figlet.renderText(prompt))
        else:
            print("Invalid Usage")
            sys.exit()
else:
    print("Invalid Usage")
    sys.exit


"""
elif len(sys.argv) == 3:
    prompt = input("Your text here: ")
    if sys.argv[1] == "-f" or "--font":
        userfont = sys.argv[2]
        if userfont in fonts:
            figlet.setFont(font=userfont)
            print(figlet.renderText(prompt))
        else:
            print("Invalid Usage")
            sys.exit
    else:
        print("Invalid Usage")
        sys.exit
"""
