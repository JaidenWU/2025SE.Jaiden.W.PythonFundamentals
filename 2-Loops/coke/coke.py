def main():
    while True:
        coin = int(input("Insert Coin: "))
        if coin == 5 or coin == 10 or coin == 25:
            remainder = 50 - coin
            print("Amount Due: ", 50 - coin)
        else:
            print("Amount Due: 50 ")
            main()


# ask user for input for how many coins they inserted
# check if input is either 5, 10, 25
# 50 - inputted value, stores this as 'remainder'
# print 50 - inputted value
# repeat this but instead of 50 use 'remainder'


main()
