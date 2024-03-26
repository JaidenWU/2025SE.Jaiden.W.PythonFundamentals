# expects exactly one command-line argument
# exactly one command-line argument,
# or if the specified file’s name does not end in .py,
# or if the specified file does not exist, the program should instead exit via sys.exit.


import sys

lines = 0

# exceptions here
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
prompt = sys.argv[1]
if not prompt.endswith(".py"):
    print("Not a Python file")
    sys.exit()

try:
    with open(prompt) as file:
        for line in file:
            line = line.strip()
            if line.startswith("#"):
                lines += 0
            elif not line:
                lines += 0
            else:
                lines += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(f"Number of lines: {lines}")


# Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
# Assume that any line that only contains whitespace is blank.
