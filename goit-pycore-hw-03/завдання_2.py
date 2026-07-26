import random


def get_numbers_ticket(min, max, quantity):
    
    if min < 1 or max > 1000:
        return []

    if quantity > (max - min + 1) or quantity <= 0:
        return []

    # унікальні
    numbers = random.sample(range(min, max + 1), quantity)

    numbers.sort()

    return numbers

lottery_numbers = get_numbers_ticket(1, 47, 5)
print("Ваші лотерейні числа:", lottery_numbers)