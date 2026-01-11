a = list(map(int, input().split()))

largest = second = float('-inf')  # Initialize very small

for num in a:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)
