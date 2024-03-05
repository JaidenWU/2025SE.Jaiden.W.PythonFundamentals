months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    try:
        print("Give me a date ")
        date = input().replace(",", "").replace("/", " ").title()
        m, d, y = date.split()
        d = int(d)
        if m[0].isdigit():
            m = int(m)
            if m <= 12 and d <= 31:
                m = int(m)
                print(f"{y:04}-{m:02}-{d:02}")
                break
            else:
                pass
        if m in months:
            m = months.index(m) + 1
            if m <= 12 and d <= 31:
                print(f"{y:04}-{m:02}-{d:02}")
                break
            else:
                pass
    except ValueError:
        pass
