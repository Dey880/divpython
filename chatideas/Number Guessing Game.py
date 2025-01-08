import random

secretNumber = random.randint(0, 100)

while True:
    guess = input("Guess a number between 0 and 100:   ")
    guess = int(guess)
    if guess != secretNumber:
        if guess >= secretNumber:
            print("too high")
        if guess <= secretNumber:
            print("too low")
    else:
        print("correct")
        break