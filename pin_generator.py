import random
print("Random password generator 1-10, with flexible length")
print("")
a = "12345678910"
b = int(input("what is the length: "))
x = "".join(random.choice(a) for i in range(b))
print(x)
