while True:
    print("Examples: addition, subtraction, multiplication, division")
    math = input("What type of math is it")
    if math == "addition":
        def add(a, b):
            return (a + b)
        a = int(input('Enter 1st number: '))
        b = int(input('Enter 2nd number: '))
        print(f'Sum of {a} and {b} is {add(a, b)}')
    if math == "subtraction":
        def subtract(a, b):
            return (a - b)
        a = int(input('Enter 1st number: '))
        b = int(input('Enter 2nd number: '))
        print(f'Sum of {a} and {b} is {subtract(a, b)}')
    if math == "multiplication":
        def multiply(a, b):
            return (a * b)
        a = int(input('Enter 1st number: '))
        b = int(input('Enter 2nd number: '))
        print(f'Sum of {a} and {b} is {multiply(a, b)}')
    if math == "division":
        def divide(a, b):
            return (a / b)
        a = int(input('Enter 1st number: '))
        b = int(input('Enter 2nd number: '))
        print(f'Sum of {a} and {b} is {divide(a, b)}')