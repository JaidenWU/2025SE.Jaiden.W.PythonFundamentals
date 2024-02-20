def main():
    amount = 0
    while True:
        coin = int(input("Insert Coin: "))
        if coin != 5 and coin != 10 and coin != 25:
            print("Amount Due: ", 50 - amount)
        else:
            amount += coin
            due = 50 - amount
            if due > 0:
                print("Amount Due: ", due)
            elif due < 0:
                print("Change Owed: ", amount - 50)
                break
            elif due == 0:
                print("Change Owed: ", amount - 50)
                break


# ask user for input for how many coins they inserted
# check if input is either 5, 10, 25
# 50 - inputted value, stores this as 'remainder'
# print 50 - inputted value
# repeat this but instead of 50 use 'remainder'


main()
