# modules in Python

import math_operations                      #to import from other scripts
import dictionary


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(math_operations.additions(num1, num2))

print(math_operations.subtraction(num1, num2))

print(math_operations.multiplaction(num1, num2))

print(math_operations.division(num1, num2))

print()


who_is_hero = dictionary.learn_the_dictionary['hero']
print(dictionary.learn_the_dictionary)
print(who_is_hero)
print()