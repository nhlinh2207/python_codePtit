import math


def check(sum):
    if sum%3 == 0:
        return "YES"
    return "NO"
n = int(input())
while n>0:
    num = input();
    sum = 0
    for i in num:
        sum+=int(i)
    print(check(sum))
    n-=1