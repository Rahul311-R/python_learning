class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        super().show()  # Call parent method
        print("Child method")

c = Child()
c.show()
