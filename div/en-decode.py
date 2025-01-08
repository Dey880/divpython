import os

clear = lambda: os.system("clear")
clear()
alphabet_lower = "abcdefghijklmnopqrstuvwxyzæøå"
alphabet_upper = alphabet_lower.upper()

def encode(message, key):
    encoded_message = ""
    for letter in message:
        if letter in alphabet_lower:
            pos = alphabet_lower.find(letter)
            newpos = (pos + key) % len(alphabet_lower)
            encoded_message += alphabet_lower[newpos]
        elif letter in alphabet_upper:
            pos = alphabet_upper.find(letter)
            newpos = (pos + key) % len(alphabet_upper)
            encoded_message += alphabet_upper[newpos]
        else:
            encoded_message += letter
    return encoded_message
    
def decode(message, key):
    decoded_message = ""
    for letter in message: 
        if letter in alphabet_lower:
            pos = alphabet_lower.find(letter)
            newpos = (pos - key) % len(alphabet_lower)
            decoded_message += alphabet_lower[newpos]
        elif letter in alphabet_upper:
            pos = alphabet_upper.find(letter)
            newpos = (pos - key) % len(alphabet_upper)
            decoded_message += alphabet_upper[newpos]
        else:
            decoded_message += letter
    return decoded_message
    
e_d = input("Encode or decode?   ")

seed = int(input("Seed(int):   "))
print("do a number :P")
encode()
message = input("Message:   ")

encoded_message = encode(message, seed)
decoded_message = decode(message, seed)

if e_d.lower() == "encode":
    print("\nEncoded:   " + encoded_message)
elif e_d.lower() == "decode":
    print("\nDecoded:   " + decoded_message)
