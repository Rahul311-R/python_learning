try:
    a = int(input("Enter a number: "))
    print(10 / a)
except ZeroDivisionError:
    print("You can't divide by zero.")
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    print("No errors found.")
finally:
    print("Program finished.")
