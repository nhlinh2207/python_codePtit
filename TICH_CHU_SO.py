import math


def check(sum):
    if sum%3 == 0:
        return "YES"
    return "NO"
n = int(input())
while n>0:
    num = input();
    sum = 1
    for i in num:
        if i != "0":
            sum*=int(i)
    print(sum)
    n-=1