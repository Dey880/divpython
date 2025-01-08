import random
import os
import time

clear = lambda: os.system("cls")

moves = ["ROCK", "PAPER", "SCISSOR"]


while True:
    if input("Do you want to play rock paper scissors? (y/n)") != "y":
        break
    print("yay")
    time.sleep(1)
    clear()
    machine = random.choice(moves)
    user = input("enter a move:(rock, paper, scissor)   ")
    user = user.upper()
    print("USER VS MACHINE")
    time.sleep(1)
    print(f"{user} VS {machine}")
    time.sleep(1)
    if user == "ROCK" or user == "PAPER" or user == "SCISSOR":
        if user == machine:
            print("its a tie")
        elif user == "ROCK" and machine == "PAPER":
            print("machine won")
        elif user == "ROCK" and machine == "SCISSOR":
            print("user won")
        elif user == "PAPER" and machine == "ROCK":
            print("user won")
        elif user == "PAPER" and machine == "SCISSOR":
            print("machine won")
        elif user == "SCISSOR" and machine == "ROCK":
            print("machine won")
        elif user == "SCISSOR" and machine == "PAPER":
            print("user won")
        time.sleep(1)
        clear()
    else:
        print("not a valid answer")
print("aww")