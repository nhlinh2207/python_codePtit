import math

def ucln(a, b):
    n, m = a, b
    while n!= m:
        if n > m:
            n-=m
        else:
            m-=n
    return m

def check(sum):
   if sum < 2:
       return 0
   else:
       for i in range(2,int(math.sqrt(sum))+1):
           if sum%i == 0:
               return 0
       return 1
n = int(input())
while n>0:
    num = input();
    rnum = ""
    for i in range(len(num) - 1, -1, -1):
        rnum += num[i]
    if ucln(int(num), int(rnum)) == 1:
        print("YES")
    else:
        print("NO")
    n-=1