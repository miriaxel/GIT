import random

random_numbers = [random.randint(1,100) for _ in range(10)]

print("Unsorted List:")
print(random_numbers)

sorted_numbers = sorted(random_numbers)

print("Sorted List:")
print(sorted_numbers)
print("hi!")
