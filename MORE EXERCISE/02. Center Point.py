import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def get_distance(_x: float, _y: float) -> float:
    distance = math.sqrt((_x ** 2) + (_y ** 2))
    return distance


point_1 = get_distance(x1, y1)
point_2 = get_distance(x2, y2)

if point_1 <= point_2:
    print(f'({int(math.floor(x1))}, {int(math.floor(y1))})')
else:
    print(f'({int(math.floor(x2))}, {int(math.floor(y2))})')
