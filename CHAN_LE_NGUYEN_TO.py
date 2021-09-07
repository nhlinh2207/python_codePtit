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
    sum = 0
    for i in num:
        sum += int(i)
    if check(sum) == 0:
        print("NO")
    else:
        c = 0
        for i in range(0,len(num),2):
            if int(num[i]) % 2 != 0:
                c = 1
        for i in range(1,len(num),2):
            if int(num[i]) % 2 == 0:
                c = 1
        if c == 0:
            print("YES")
        else:
            print("NO")
    n-=1