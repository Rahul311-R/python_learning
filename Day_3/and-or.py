a = int(input("Enter the first num:"))
b = int(input("Enter the second num:"))

if a>=0 and b>=0:
    print("Both numbers are positive")
elif a>0 or b>0:
    print("At least one number is positive")
else:
    print("No positive numbers")