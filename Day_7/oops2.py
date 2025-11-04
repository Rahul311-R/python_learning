class Mobile:
    made_in = "India"  # class variable (common for all)

    def __init__(self, brand, price):
        self.brand = brand      # instance variable
        self.price = price

    @classmethod
    def change_country(cls, country):
        cls.made_in = country   # change for all objects

    @staticmethod
    def greet():
        print("Welcome to Mobile Store!")

# create objects
m1 = Mobile("Samsung", 20000)
m2 = Mobile("iPhone", 80000)

m1.greet()  # static method
print(m1.brand, m1.price, m1.made_in)

Mobile.change_country("Vietnam")
print(m2.brand, m2.price, m2.made_in)
