import math


def check(a):
    if a < 2:
        return 0
    for i in range(2,int(math.sqrt(a))+1):
        if a%i == 0:
            return 0
    return 1
x = [int(i) for i in input().split()]
list = []
for i in range(0,x[0]):
   a = [int(i) for i in input().split()]
   list.append(a)
for i in range(0,len(list)):
    for j in range(0,len(list[i])):
        if(check(list[i][j]) == 1):
            list[i][j] = 1
        else:
            list[i][j] = 0
for i in range(0,len(list)):
    for j in range(0,len(list[i])):
        print(list[i][j],end=" ")
    print()
