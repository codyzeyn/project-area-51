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
        randnum = ran.randint(1, 50)
        for letter in ["processing", ".", ".", ".", ".", "."]:
            print(letter, end="", flush=True)
            time.sleep(0.5)
        print()
        x = int(input("guess the number: "))
        print("the lucky number is: ", randnum)
        if randnum == x:
            print("You won!!")
            break
        else:
            print("you lost, try again.")
            x = input("press enter to try again... otherwise type something --> ")
            if x != "":
                break
