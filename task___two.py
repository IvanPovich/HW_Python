import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    if min >= 1 and max <= 1000 and quantity <= (max - min + 1):
        numbers = random.sample(range(min, max + 1), quantity)
        numbers.sort()
        return numbers
    else:
        return []

# Example
min_val = 4
max_val = 80
random_quantity = 15

random_ticket = get_numbers_ticket(min_val, max_val, random_quantity)
print(f"Випадкові квитки: {random_ticket}")
