import time
print("[ Mini Python Quiz Game ]")
print("")
x = input("ARE YOU READY? yes or no --> ").lower()
score = 0
if x == "yes":
    print("[ true or false ]")
    y = input("1. humans are mammals --> ").lower()
    if y == "true":
        score += 1
    time.sleep(2)
    print("")
    z = input("2. rice are not healthy --> ").lower()
    if z == "false":
        score += 1
    time.sleep(2)
    print("")
    x = input("3. cats are animals --> ").lower()
    if x == "true":
        score += 1
    time.sleep(2)
    print("")
    f = input("4. science is based on belief --> ").lower()
    if f == "false":
        score += 1
    time.sleep(2)
    print("")
    i = input("5. killing is bad --> ").lower()
    if i == "true":
        score += 1
    print("total score is", score)
else:
    print("what?")
