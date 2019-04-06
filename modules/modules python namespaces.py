import random

numbers_a = range(1, 13)
numbers_b = []
for i in numbers_a:
    number = random.choice(range(1000))
    numbers_b.append(number)

