import os

todo = []

while True:
    os.system("cls")
    print("""
        What do you want to do? 
        (a: view to-do list)
        (b: add item)
        (c: remove item)
    """)
    thing = input("         ")
    
    if thing == "a" or thing == "b" or thing == "c":
        if thing == "a":
            print(f"         {todo}")
            input()
        elif thing == "b":
            add = input("         what do you want to add:   ")
            todo.append(add)
        elif thing == "c":
            if len(todo) >= 1:
                print(f"         {todo}")
                remove = input("         what do you want to remove:    ")
                remove = int(remove)
                remove -= 1
                todo.pop(remove)
                print(f"         {todo}")
            else:
                print("cannot remove from empty list")
                input()
    else:
        print("unknown command")