class car:
    wheels = 4
    def __init__(self,model,year):
        self.model = model
        self.year = year

    def old(self):
        return f"The car is {self.year} old"

    def name(self):
        return f"The brand is {self.model}"


m = input()
n = int(input())
a1 = car(m,n)
print(a1.old())
print(a1.name())
print(a1.wheels)