COFFEE = 1.50
WATER = 1.00
COKE = 1.40
SNACKS = 2.00

order = input()
quantity = int(input())


def billed(item: str, qty: int) -> float:
    bill = 0.00
    if item == 'COFFEE':
        bill = COFFEE * qty
    elif item == 'WATER':
        bill = WATER * qty
    elif item == 'COKE':
        bill = COKE * qty
    elif item == 'SNACKS':
        bill = SNACKS * qty
    return bill


print(f'{billed(str.upper(order), quantity):0.2f}')
