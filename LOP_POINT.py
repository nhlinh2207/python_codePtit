import math


class Decimal:
    value: float

    def __init__(self, a):
        self.value = float(a)

class Point:
    x: Decimal
    y: Decimal

    def __init__(self,x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        a = math.sqrt(math.pow(self.x.value - point.x.value, 2) + math.pow(self.y.value - point.y.value, 2))
        return "{:.4f}".format(a)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1

