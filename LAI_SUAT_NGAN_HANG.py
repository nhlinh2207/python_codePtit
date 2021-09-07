num = int(input())
while num > 0:
   x = [float(i) for i in input().split()]
   c = 0
   while x[0]<x[2]:
      c = c+1
      x[0] = x[0]+x[0]*x[1]/100
   print(c)
   num -= 1