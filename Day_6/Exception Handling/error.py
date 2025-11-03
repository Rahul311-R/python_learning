try:
    a = int(input())
    b = int(input())
    res = a/b
    print(res)
except ValueError:
    print("That’s not a valid number.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")