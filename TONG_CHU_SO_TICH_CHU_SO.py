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
    tong = 0
    tich = 1
    c = 0
    for i in range(0,len(num)):
        if i%2 == 0:
            tong += int(num[i])
        else:
            if num[i] != "0":
                c+=1
                tich *= int(num[i])
    print(tong, end=" ")
    if c == 0:
        print("0")
    else:
        print(tich)
    n-=1