import random
number = random.randint (1, 100)
hardness = input("choose a difficulty: ")
easy = 10
hard = 5

print(number)


def difficulty(test):
    if test == 'easy':
        return easy
    else:
        return hard

level = difficulty(hardness)

tries = True
# if difficulty == 'easy':   
while tries:
    print(f"you have {level} guesses left")
    guess = int(input('enter your guess: '))
    
    
    if guess == number:
        print("you guessed right you win")
        tries = False

    if guess < number:
        print("too low")

    elif guess > number:
        print('too high')   

    level -= 1
    if level == 0:
        print("you've exausted your guesses")
        tries = False

        



