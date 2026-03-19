age = int(input("Enter age: "))
full_price = 500

if age <12:
    print("Ticket is free!")
elif age>60:
    print(f"Ticket price: ₹{250}")
else:
    print(f"Ticket price: ₹{500}")