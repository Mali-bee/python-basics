#functions in Python

print()
first_name = input("Enter your first name: ")
last_name = input("Enter your surname: ")

def name(first, last):                                          #creating a function
    print(f"Greetings and a pleasure to you {first} {last}")    #use the 
    
name(first_name, last_name)
print()


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def calc(a, b):
    return a + b

results = calc(num1, num2)
print(f"The answer to the calculator is {results}")
print()

    
def greeting(name, greeting="Hello"):
    print(f"{greeting}, {name}")

name = input("Enter full name: ")

greeting(name)
print()
