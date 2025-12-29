import math
import random

print("=== Welcome to Numbers Hub ===")

# Part 1: Calculator
print("\n--- Calculator ---")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

# Part 2: Math Functions
print("\n--- Math Functions ---")
num = int(input("Enter a number for math operations: "))
print("Square root:", math.sqrt(num))
print("Factorial:", math.factorial(num))
print("Ceil:", math.ceil(num))
print("Floor:", math.floor(num))

# Part 3: Random Number Guessing Game
print("\n--- Guess the Random Number (1-100) ---")
secret = random.randint(1, 100)
guess = int(input("Enter your guess: "))
if guess == secret:
    print("Correct! You guessed the number.")
else:
    print(f"Try again! The number was {secret}")

print("\n=== Thank you for using Numbers Hub ===")
