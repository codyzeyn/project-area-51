print("[ Basic Calculator ]")
print("          | ")
a = input("are you ready? yes/no --> ").lower()
if a == "yes":
    while True:
        b = str(input("choose your operators, +, -, x, / --> "))
        n = int(input("num: "))
        nn = int(input("num: "))
        if b == "+":
            print(n + nn)
        if b == "-":
            print(n - nn)
        if b == "x":
            print(n * nn)
        if b == "/":
            print(n / nn)
        c = input("just press enter to continuee... or type something to exist --> ")
        if c != "":
            break
            
        
