#Count of even number in the List
numbers = [1,5,7,8,10,18,50]
count = 0

for n in numbers:
    if n % 2 == 0:
        count += 1

print(count)