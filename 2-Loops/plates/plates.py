def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # plates must maximum of 6 characters and minimum of 2 characters
    if len(s) < 2 or len(s) > 6:
        return False
    if not start_with_2letters(s):
        return False
    if not valid_characters(s):
        return False
    if not numbers_at_end(s):
        return False
    else:
        return True


# plate must start with at least two letters
def start_with_2letters(s):
    return s[0:2].isalpha()


# Numbers cannot be used in the middle of a plate, must come at the end. The first number used cannot be a ‘0’
def numbers_at_end(s):
    digits = ""
    for char in s:
        if char.isdigit():
            digits += char
        if digits.startswith("0"):
            return False
    if not s[-1].isdigit():
        return False
    else:
        return True


# No periods, spaces, or punctuation marks are allowed
def valid_characters(s):
    return s.isalnum()


main()
