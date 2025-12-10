age = int(input("Enter the age:"))
country = input("Enter the country:").lower()

if age>=18:
    if country == "india":
        print("Eligible to vote in India")
    else:
        print("18+ but not in India")
else:
    print("Not eligible")