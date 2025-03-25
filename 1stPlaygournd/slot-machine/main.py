import random

def spin_row():
    symbols =['🍒','🍇','🍋','⭐','🔔']

    return [random.choice(symbols) for _ in range(3)]


def print_row(row:list):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row:list,bet:int):
    if row[0] ==row[1]==row[2]:
        match row[0]:
            case '🍒':
                return bet*3
            case '🍇':
                return bet*5
            case '🍋':
                return bet*4
            case '⭐':
                return bet*10
            case '🔔':
                return bet*1.5

    return 0
            
def main():
    balance =100

    print("------------------------")
    print("Welcome to slotter game!")
    print("Symbols: 🍒🍇🍋⭐🔔")
    print("------------------------")

    while balance>0:
        print(f"Current balance ${balance}")

        bet = input("Place your bet amount:")

        if not bet.isdigit():
            print("Please enter a vlaid number")
            continue
        bet = int(bet)

        if bet >balance:
            print("Insufficient funds")
            continue

        if bet <=0:
            print("Bet must be greater than 0")
            continue

        balance -=bet
        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout= get_payout(row,bet)

        if payout>0:
            print(f"You won ${payout}")
        else:
            print("You lost this round!")
        
        balance+=payout

if __name__=='__main__':
    main()