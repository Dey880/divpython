import math

print("""
what do you want to do?
(a: add)
(b: subtract)
(c: multiply)
(d: divide)
(e: square root)
(f: power)
""")

do = input()

if do == "a" or do == "b" or do == "c" or do == "d" or do == "e" or do == "f":
    if do == "a":
        num0 = float(input("first number:   "))
        num1 = float(input("second number:   "))
        print(f"{num0} + {num1}\n{num0 + num1}")
    elif do == "b":
        num0 = float(input("first number:   "))
        num1 = float(input("second number:   "))
        print(f"{num0} - {num1}\n{num0 - num1}")
    elif do == "c":
        num0 = float(input("first number:   "))
        num1 = float(input("second number:   "))
        print(f"{num0} * {num1}\n{num0 * num1}")
    elif do == "d":
        num0 = float(input("first number:   "))
        num1 = float(input("second number:   "))
        print(f"{num0} / {num1}\n{num0 / num1}")
    elif do == "e":
        num0 = float(input("number:   "))
        print(f"sqrt({num0})\n{math.sqrt(num0)}")
    elif do == "f":
        num0 = float(input("number:   "))
        num1 = float(input("to the power of:   "))
        print()
        print(f"{num0} ^ {num1}\n{math.pow(num0, num1)}")
