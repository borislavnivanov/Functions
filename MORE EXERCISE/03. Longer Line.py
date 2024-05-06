from math import floor
from math import sqrt

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


def get_distance(_x: float, _y: float) -> float:
    distance = sqrt((_x ** 2) + (_y ** 2))
    return distance


point_1 = get_distance(x1, y1)
point_2 = get_distance(x2, y2)
point_3 = get_distance(x3, y3)
point_4 = get_distance(x4, y4)

line_1 = point_1 + point_2
line_2 = point_3 + point_4

if line_1 >= line_2:
    if point_1 <= point_2:
        print(f'({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})')
    else:
        print(f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})')
if line_1 < line_2:
    if point_3 <= point_4:
        print(f'({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})')
    else:
        print(f'({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})')
