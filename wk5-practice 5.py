numbers = [9,100,101,88,3,7]

largest = 0
second = 0

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print(second)