from datetime import date
import sys
import inflect

p = inflect.engine()


class DOB:
    def __init__(self, dob, today):
        self.dob = dob
        self.today = today

    @classmethod
    def get(cls):
        today = date.today()
        try:
            dob = date.fromisoformat(input("Date of Birth: "))
        except ValueError:
            sys.exit("Invalid Format")
        return cls(today, dob)

    def calcDiff(self):
        diff = self.dob - self.today
        diff = diff.days * 1440
        return diff


def main():
    obj = DOB.get()
    words = p.number_to_words(obj.calcDiff())
    print(f"{words} minutes")


if __name__ == "__main__":
    main()
