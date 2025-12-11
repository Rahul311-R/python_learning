try:
    n = int(input("Enter a number:"))
    print(10/n)
except ValueError:
    print("please enter a integer!")
except ZeroDivisionError:
    print("Zero can not be divided")
finally:
    print("print will done at final")