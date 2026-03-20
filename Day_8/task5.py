marks = [78, 92, 56, 92, 78, 88, 92, 71, 56, 78]
a = marks.count(92)
b = marks.count(78)
c = marks.count(56)
if a > b and a > c:
    print("92 appears more time")
elif b > a and b > c:
    print("78 appears more time")
else:
    print("56 appears more time")
print(f"92 appears {a} times")
print(f"78 appears {b} times")
print(f"56 appears {c} times")