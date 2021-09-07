import math


def check(a):
    if a < 2:
        return 0
    for i in range(2,int(math.sqrt(a))+1):
        if a%i == 0:
            return 0
    return 1
x = input() #int(input()) #[int(i) for i in input().split()]
print("Hello "+x+"!")