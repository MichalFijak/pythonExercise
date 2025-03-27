import random
# nubmer = random.randint(1,6)

# options = ("rock","paper","scissors")
# option =random.choice(options)

lowest_num=1
highest_num=10
guesses = 0
is_running =True

selected_number = random.randint(lowest_num,highest_num)

while is_running:
    answer = input("Enter your number:")
    guesses+=1
    if answer.isdigit() and lowest_num<=int(answer)<=highest_num:
        if(int(answer)==selected_number):
            print(f"You have won at cost of {guesses} tries!")
            is_running=False
        else:
            print("Guess again!")
    else:
        print("You put wrong number!")
