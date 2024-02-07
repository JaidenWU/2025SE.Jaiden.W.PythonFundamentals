def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # strip dollar sign and one zero
    D = float(d.removeprefix("$").removesuffix("0"))
    return D


def percent_to_float(p):
    # strip percentage sign and divide by 100
    P = float(p.removesuffix("%")) / 100
    return P


main()
