def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # strip dollar sign
    d = d.removeprefix("$")
    return float(d)


def percent_to_float(p):
    p = p.replace("%", "")
    return float(p)


main()
