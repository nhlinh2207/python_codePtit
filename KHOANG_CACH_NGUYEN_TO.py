import math


def check(a):
   if a< 2:
       return 0
   for i in range(2,int(math.sqrt(a))+1):
       if a%i == 0:
           return 0
   return 1
val = [int(i) for i in input().split()]
list1 = []
n = val[0]
x = val[1]
list1.append(x)
nt = 2
while len(list1) <n+1:
    while check(nt) == 0:
        nt+=1
    list1.append(list1[len(list1)-1]+nt)
    nt+=1
for i in list1:
    print(i, end=" ")
print()