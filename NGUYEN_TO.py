import math


def ntcn (x,y):
    k = 0
    for i in range (x, 0, -1):
        if x%i ==0 and y%i ==0:
            k = i
            break
    if k ==1:
        return 1
    else:
        return 0

num = int(input())
while num > 0:
    x = int(input())
    c = 0
    for i in range(1,x):
        if(ntcn(i, x) == 1):
           c += 1
    if c< 2:
        print("NO")
    else:
        d = 0
        for i in range (2, int(math.sqrt(c))+1):
            if c%i ==0 :
                print("NO")
                d = 1;
                break
        if d == 0:
            print("YES")

    num -= 1