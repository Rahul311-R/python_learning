def check_age(age):
    if age>=18:
        return "adult"
    elif 13<=age<18:
        return "teen"
    else:
        return "Child"
    

a = int(input("Enter the age:"))
print(check_age(a))