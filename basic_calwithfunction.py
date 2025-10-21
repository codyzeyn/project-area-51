import time

for letters in ["-- Basic ", "Calculator ", "that ", "involves ", "Functions --"]:
	print(letters, end="", flush= True)
	time.sleep(0.5)
print()
print("")
a = input("are you ready? yes/no --> ").lower()
if a == "yes":
	while True:
		operator = input("add, sub, multi, divi? --> ").lower()
		num1 = int(input("num: "))
		num2 = int(input("num: "))
		def add():
			return num1 + num2
		def sub():
		    return num1 - num2
		def multi():
		     return num1 *  num2
		def divi():
		     return num1 / num2
		if operator == "add":
			print(add())
		elif operator == "sub":
			print(sub())
		elif operator == "multi":
			print(multi())
		elif operator == "divi":
			print(divi())
		again = input("press enter to continue...")
		if again != "":
			break
	else:
		print("what do you mean?")