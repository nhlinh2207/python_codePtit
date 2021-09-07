import math


def check(sum):
   if sum < 2:
       return "NO"
   else:
       for i in range(2,int(math.sqrt(sum))+1):
           if sum%i == 0:
               return "NO"
       return "YES"
n = int(input())
while n>0:
    num = input();
    val = ""
    for i in range(len(num) - 4,len(num)):
        val+=num[i]
    print(check(int(val)))
    n-=1