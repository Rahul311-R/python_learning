pwd = input("Enter the password:")
if len(pwd)>=8 and pwd.isalnum():
    print("String password")
else:
    print("weak password")