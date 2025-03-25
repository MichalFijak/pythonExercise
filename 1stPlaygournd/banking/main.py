


def show_balance():
    print(f"Your balance equals: {balance : .2f} Galleons")

def deposit():
    amount= input("How much you want to deposit?")
    if amount.isdigit() and float(amount)>0:
        return float(amount)
    else:
        print("I expecting REAL money!")

def withdraw():
    amount= input("How much you want to withdraw?")
    if amount.isdigit():
        if balance -float(amount) <0:
            print("You dont have enough money to do so!")
            return 0
        else:
            print("Here's yours money!")
            return float(amount)
    else:
        print("I expecting REAL money!")


balance=0
is_running = True

while is_running:
    print("---------------Gringotss bank---------------")
    print("---------------1.Show balance---------------")
    print("----------------2.Deposit-------------------")
    print("----------------3.Withdraw------------------")
    print("-----------------4.Exit---------------------")

    choice = input("Enter you choice (1-4):")

    if choice.isdigit():
        match int(choice):
            case 1:
                show_balance()
            case 2:
                balance +=deposit()
            case 3:
                balance -=withdraw()
            case 4:
                print("Thank you for your service!")
                is_running=False
    else:
        print("Enter a number from range (1-4)")