import random
import time
import os

NUMBER_MAX = 100
NUMBER_MIN = 0
OVER = 1
UNDER = 0
CORRECT = 2

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def play_guessing_game():
    number_max = NUMBER_MAX
    number_min = NUMBER_MIN
    guesses = 1
    win = False
    
    print("Think of a number between 0 and 100")
    
    while not win:
        try:
            clear()
            if number_max - number_min <= 1:
                print("The number range is impossible. Please restart the game.")
                return
                
            number = random.randint(number_min + 1, number_max - 1)
            print(f"Guessing a number between {number_min} and {number_max}...")
            time.sleep(0.5)
            guess = input(f"Is the number over or under {number} (1 for over, 0 for under, if the number is correct type 2): ")
            
            if not guess.isdigit():
                raise ValueError("Input must be a number.")
                
            guess = int(guess)
            
            if guess == UNDER or guess == OVER:
                guesses += 1
                if guess == UNDER:
                    number_max = number
                elif guess == OVER:
                    number_min = number
            elif guess == CORRECT:
                print(f"Your number was {number}, and it was guessed in {guesses} guesses.")
                win = True
            else:
                raise ValueError("Invalid option.")
                
        except ValueError as e:
            print(f"Error: {e}. Please enter 0, 1, or 2.")
            time.sleep(2)
            
play_guessing_game()