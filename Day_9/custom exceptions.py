age = int(input("Enter your age: "))

if age < 18:
    raise Exception("Access denied — you must be 18 or older.")
else:
    print("Access granted.")


class UnderAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise UnderAgeError("You are too young.")
    else:
        print("Welcome!")
except UnderAgeError as e:
    print("Custom Error:", e)
