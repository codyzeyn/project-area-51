import random as ran
import time
print("< lottery game simulation !!! >")
print("")
a = input("are you ready? yes/no --> ").lower()
if a == "yes":
    print("the lucky winner number is between 1-50")
    print("")
    input("press enter to start....")
    while True:
        randlist = ran.randint(1, 50)
        for letter in ["randomizing", ".", ".", ".", ".", "."]:
            print(letter, end="", flush=True)
            time.sleep(0.5)
        print()
        print("the number you got is:", randlist)
        if randlist == 38:
            print("You won!!")
            break
        else:
            print("you lost, try again.")

