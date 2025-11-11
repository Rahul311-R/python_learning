class Student:
    def __init__(self, name, age):
        self.name = name          # public attribute
        self.__age = age          # private attribute (encapsulated)

    def get_age(self):
        return self.__age         # getter method

    def set_age(self, age):
        if age > 0:
            self.__age = age      # setter method
        else:
            print("Invalid age")

s = Student("Rahul", 20)
print(s.name)           # accessible
print(s.get_age())      # access private data safely

s.set_age(22)
print(s.get_age())

# print(s.__age) → ❌ will cause error (private variable)
