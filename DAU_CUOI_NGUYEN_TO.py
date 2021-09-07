import math


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
    dau = ""
    cuoi = ""
    dau += (num[0]+num[1]+num[2])
    cuoi += (num[-3]+num[-2]+num[-1])
    if check(int(dau)) == 1 and check(int(cuoi)) == 1:
        print("YES")
    else:
        print("NO")
    n-=1