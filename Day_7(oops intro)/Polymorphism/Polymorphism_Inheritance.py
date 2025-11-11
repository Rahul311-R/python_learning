class Bird:
    def intro(self):
        print("There are many types of birds")

    def flight(self):
        print("Most birds can fly")

class Penguin(Bird):
    def flight(self):
        print("Penguins can’t fly, they swim")

p = Penguin()
p.intro()
p.flight()
