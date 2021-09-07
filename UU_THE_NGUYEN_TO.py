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
    if check(len(num)) == 0:
        print("NO")
    else:
        nt = 0
        knt = 0
        for i in num:
            if check(int(i)) == 0:
                knt += 1
            else:
                nt+=1
        if nt > knt:
            print("YES")
        else:
            print("NO")
    n-=1