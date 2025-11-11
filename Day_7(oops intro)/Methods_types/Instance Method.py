class fruit:
    def __init__(self,name):
        self.name = name

    def say(self):
        print("The name of the fruit is",self.name)


a = input()
a1 = fruit(a)
a1.say()