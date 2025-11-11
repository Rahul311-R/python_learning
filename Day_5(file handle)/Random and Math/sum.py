import math, random

def random_circle_area():
    a = random.randint(1, 10)
    area = math.pi * a * a
    print(f"Radius: {a}, Area: {area:.2f}")

random_circle_area()
