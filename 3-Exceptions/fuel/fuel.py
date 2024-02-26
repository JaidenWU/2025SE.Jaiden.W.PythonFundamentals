while True:
    try:
        prompt = input("What's the fuel gauge in a fraction ")
        X, Y = prompt.split(sep="/")
        X = int(X)
        Y = int(Y)
        output = (X / Y) * 100
        output = int(round(output, 1))
        if output <= 1:
            print("E")
        elif 100 >= output >= 99:
            print("F")
        elif output > 100:
            continue
        else:
            print(f"{output}%")
        break
    except (ValueError, ZeroDivisionError):
        pass
