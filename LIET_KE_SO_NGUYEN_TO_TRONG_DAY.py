import math


def check(a):
   if a< 2:
       return 0
   for i in range(2,int(math.sqrt(a))+1):
       if a%i == 0:
           return 0
   return 1
num = int(input())
val = [int(i) for i in input().split()]
list1 = []
for i in val:
    if check(i) == 1 and not i in list1:
        print(str(i)+" "+str(val.count(i)))
        list1.append(i)