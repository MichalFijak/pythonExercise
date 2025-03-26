import random

words = ("apple", "orange","banana","coconut")


hangman_art={0:("   ",
                "   ",
                "   "),
             1:(" o ",
                "   ",
                "   " ),
             2:(" o ",
                " | ",
                "   "),
             3:(" o ",
                "/| ",
                "   "),
             4:(" o ",
                "/|\\",
                "   "),
             5:(" o ",
                "/|\\",
                "/  "),
             6:(" o ",
                "/|\\",
                "/ \\")}

def display_man(wrong:int):
    for line in hangman_art[wrong]:
        print(line)


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint=["_"] * len(answer)
    still_in_game = True
    mistakes=0
    guessed_letter=set()

    while still_in_game:
        display_man(mistakes)
        display_hint(hint)
        guess = input("Guess letter!").lower()
        
        if len(guess)!=1 or not guess.isalpha():
            print("Invalid input!")
            continue
        
        if guess in guessed_letter:
            print(f"{guess} is already guessed")
            continue
        
        if guess not in answer:
            mistakes+=1
            print("Wrong letter")

        else:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i] = guess
                    guessed_letter.add(guess)
        
        if "_" not in hint:
            print("You win!")
            display_answer(answer)
            still_in_game=False

        if mistakes==len(hangman_art)-1:
            display_man(mistakes)
            print("You lose!")
            still_in_game=False
        
if __name__ =="__main__":
    main()


