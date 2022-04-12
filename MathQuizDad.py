import time
print("Hello")
time.sleep(1)
print("Welcome To the Math Quiz")
time.sleep(1)
print("My name is PY")
time.sleep(1)
name = input("What is your name?")
print("Hello", name)
time.sleep(1)

num1 = int(input("Please type in your first number"))
num2 = int(input("Please type in your second number"))
choosemathtype = input("Please type your math equation type: Examples: Addition, Subtraction, Multiplication, and Division")

if choosemathtype == "Addition":
    print("Ok")
    sum= num1 + num2
    print("The answer is " + str(sum))

if choosemathtype == "Subtraction":
    print("Ok")
    print("The answer is " - str(sum))

if choosemathtype == "Multiplication":
        print("Ok")
        print("The answer is " * str(sum))

if choosemathtype == "Division":
    print("Ok")
    print("The answer is", str(sum))