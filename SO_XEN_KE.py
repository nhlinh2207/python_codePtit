import math


def check(sum):
    if len(sum) %2 == 0:
        return "NO"
    else:
        if sum[0] == sum[1]:
            return "NO"
        else:
            val = sum[0]
            for i in range(2,len(sum),2):
                if sum[i] != val:
                    return "NO"
            return "YES"
n = int(input())
while n>0:
    num = input();
    sum = 1
    for i in num:
        if i != "0":
            sum*=int(i)
    print(check(num))
    n-=1