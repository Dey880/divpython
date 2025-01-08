import random
import time
import os

MIN_NUMBER = 0
MAX_NUMBER = 100

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def play_guessing_game():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    win = False
    guesses = 0
    current_min = MIN_NUMBER
    current_max = MAX_NUMBER
    
    print("Welcome to the number guessing game!")
    
    while not win:
        try:
            guess = input(f"Guess a number from {current_min} to {current_max}: ")
            guess = int(guess)
            
            if guess < current_min or guess > current_max:
                print(f"Please guess a number within the valid range ({current_min} to {current_max}).")
                continue
                
            guesses += 1
            
            if guess == number:
                print("Correct!")
                win = True
            elif guess < number:
                print("Too low.")
                current_min = guess
            elif guess > number:
                print("Too high.")
                current_max = guess
                
            time.sleep(1)
            clear()
            
        except ValueError:
            print("Not a valid number, please try again.")
            
    print(f"You guessed the number {number} in {guesses} guesses.")
    
play_guessing_game()