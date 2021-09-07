
num = int(input())
while num > 0:
   x = [int(i) for i in input().split()]
   list = [1,1]
   a = b =1
   for i in range (3,93):
       c = a+b
       a = b
       b = c
       list.append(b)
   for i in range (x[0], x[1] + 1):
       print(list[i-1], end=" ")
   print()
   num -= 1