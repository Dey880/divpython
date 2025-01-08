import random
import string
import os

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits = list(string.digits)
specialCharacters = list("!@#$%^&*()")
characters = []
password = []

length = int(input("how long do you want your password to be?   "))
type = input("what type of characters do you want: (a: lowercase, b: uppercase, c: numbers, d: special characters)   ")

if "a" in type:
    characters += lowercase
if "b" in type:
    characters += uppercase
if "c" in type:
    characters += digits
if "d" in type:
    characters += specialCharacters
    
for n in range(length):
    password.append(random.choice(characters))
password = ''.join(password)
# os.system("cls")
print(password)