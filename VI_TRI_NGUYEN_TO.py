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
    c = 0
    for i in range (0,len(num)):
         if check(i) == 1:
             if check(int(num[i]))== 0:
                 c = 1
         if check(i) == 0:
             if check(int(num[i])) == 1:
                 c = 1
    if c== 0:
        print("YES")
    else:
        print("NO")
    n-=1