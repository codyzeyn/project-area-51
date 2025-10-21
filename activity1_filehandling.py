import time
import sys


def create():
    with open("activity_1.txt", "w") as file:
        file.write("hello this is my activity 1")

def read():
    with open("activity_1.txt", "r") as file:
        text = file.read()
        print(text)


act = "This is my Activity 1 that writes a file and reads it"
for letter in act:
    print(letter, end="", flush=True)
    time.sleep(0.2)
print()

a = input("create a file. yes or no? --> ").lower()
if a == "yes":
    create()
    read()
else:
    sys.exit()