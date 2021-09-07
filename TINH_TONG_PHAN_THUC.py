import math

def ucln(a, b):
    if (b == 0):
        return a;
    return ucln(b, a % b)

def check(sum):
   if sum < 2:
       return 0
   else:
       for i in range(2,int(math.sqrt(sum))+1):
           if sum%i == 0:
               return 0
       return 1
num = int(input())
while num > 0:
    val = int(input())
    if val%2 == 0:
        sum = 0
        for i in range(2, val+1, 2):
            sum += 1/i
        print("{:.6f}".format(sum))
    if val%2 == 1:
        sum = 0
        for i in range(1, val+1, 2):
            sum += 1/i
        print("{:.6f}".format(sum))
    num-=1