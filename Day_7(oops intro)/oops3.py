class clg:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def id(self):
        return self.name

    def reg(self):
        return self.age

a1 = input()
a2 = int(input())
d = clg(a1,a2)
print("the name is",d.id())
print("the age is",d.reg())
