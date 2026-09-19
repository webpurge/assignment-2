import random

numbers = [random.uniform(0, 10) for _ in range(5)]

print("Generated numbers:", numbers)
print("Minimum value:", min(numbers))
print("Maximum value:", max(numbers))
