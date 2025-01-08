import time
from random import choice
import os

try:
    point = int()
    play = input("Do you want to play?  y/n:  ")
    while play == "y":
    
        clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
        
        word = choice([
            "code", "course", "jazz", "ring", "hangman", "summer vacation", "robot", "club",
            "church", "concentrate", "doctor", "focus", "norway", "banana", "christian", "pc",
            "charger", "age", "storage", "keyboard", "percent", "sunflower", "memory",
            "axe", "flower", "cut", "sit", "lie", "guess", "word", "cold",
            "night", "day", "head", "arm", "leg", "stomach", "blanket", "sofa", "button",
            "pillow", "table", "tv", "cage", "electricity", "washing machine", "microwave",
            "speaker", "basket", "jacket", "bottle", "lunch box", "apple", "cherry",
            "computer", "school", "puzzle", "library", "universe", "galaxy", "cloud",
            "python", "programming", "network", "server", "game", "adventure", "travel",
            "music", "art", "science", "future", "knowledge", "creativity", "forest", "mountain",
            "river", "ocean", "beach", "sunset", "moonlight", "star", "planet", "astronaut",
            "spaceship", "alien", "robotics", "technology", "innovation", "hacker", "cyber",
            "binary", "algorithm", "data", "security", "encryption", "password", "firewall",
            "matrix", "quantum", "gravity", "dimension", "energy", "light", "shadow", "wind",
            "storm", "volcano", "earthquake", "nature", "wildlife", "ecosystem", "biodiversity",
            "meditation", "mindfulness", "harmony", "balance", "zen", "philosophy", "wisdom",
            "history", "myth", "legend", "fantasy", "magic", "wizard", "dragon", "castle",
            "kingdom", "journey", "quest", "hero", "villain", "treasure", "mystery"
        ])
        guessed = []
        wrong = []
        guesses = int()
        
        tries = 8
        clear()
        
        while tries > 0:
            out = ""
            for letter in word:
                if letter in guessed:
                    out = out + letter
                else:
                    out = out + "_ "
                    
            if out == word:
                break
                
            print(f"Guess a letter in the word {out}")
            print(f"{tries} tries left")
            
            try:
                guess = input()
                int(guess)
                
            except(ValueError):
                guess = guess.lower()
                
                if guess in guessed or guess in wrong:
                    clear()
                    print(f"The letter '{guess}' is already guessed")
                elif guess in word:
                    clear()
                    print(f"Congratulations! the letter '{guess}' was in the word!")
                    guesses += 1
                    guessed.append(guess)
                else:
                    clear()
                    print(f"Sorry,' {guess}' was not in the word")
                    tries = tries - 1
                    guesses += 1
                    wrong.append(guess)
                    
                if tries == 7:
                    print(r" ____")
                    print(r" |  |")
                    print(r" o  |")
                    print(r"    |")
                    print(r"    |")
                    print(r"    |")
                    print(r"    |")
                elif tries == 6:
                    print(r" ____")
                    print(r" |  |")
                    print(r" o  |")
                    print(r" ^  |")
                    print(r"    |")
                    print(r"    |")
                    print(r"    |")
                elif tries == 5:
                    print(r" ____")
                    print(r" |  |")
                    print(r" o  |")
                    print(r" ^  |")
                    print(r" |  |")
                    print(r"    |")
                    print(r"    |")
                elif tries == 4:
                    print(r" ____")
                    print(r" |  |")
                    print(r" o  |")
                    print(r" ^  |")
                    print(r"/|  |")
                    print(r"    |")
                    print(r"    |")
                elif tries == 3:
                    print(r" ____")
                    print(r" |  |")
                    print(r" o  |")
                    print(r" ^  |")
                    print(r"/|\ |")
                    print(r"    |")
                    print(r"    |")
                elif tries == 2:
                    print(r" ____")
                    print(r" |  |")
                    print(r" o  |")
                    print(r" ^  |")
                    print(r"/|\ |")
                    print(r" ^  |")
                    print(r"    |")
                elif tries == 1:
                    print(r" ____")
                    print(r" |  |")
                    print(r" o  |")
                    print(r" ^  |")
                    print(r"/|\ |")
                    print(r" ^  |")
                    print(r"/   |")
                print()
                
        if tries:
            print(f"you guessed {word} with {8 - tries + 1} mistakes, and with {guesses} tries.")
        else:
            print(f"You could not guess the word {word}")
            print(r" ____")
            print(r" |  |")
            print(r" o  |")
            print(r" ^  |")
            print(r"/|\ |")
            print(r" ^  |")
            print(r"/ \ |")
        time.sleep(5)
        clear()
        play = input("Do you want to play?  y/n:  ")
        if play != "y":
            break
except(KeyboardInterrupt):
    clear()
    quit()
clear()