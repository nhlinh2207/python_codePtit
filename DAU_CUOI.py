import math


def check(a):
    if a < 2:
        return 0
    for i in range(2,int(math.sqrt(a))+1):
        if a%i == 0:
            return 0
    return 1
x = int(input()) #[int(i) for i in input().split()]
while x>0:
    s = input()
    a = int(s[0:2])
    b = int(s[len(s)-2:])
    if a == b:
        print("YES")
    else:
        print("NO")
    x-=1