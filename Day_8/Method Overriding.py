class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()   # Output: Dog barks
