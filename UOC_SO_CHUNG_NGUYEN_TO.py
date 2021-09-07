import math

num = int(input())
while num > 0:
   x = [int(i) for i in input().split()]
   c = -1
   d = -1
   if x[0] < x[1]: c = x[0]
   else: c = x[1]
   for i in range(c, 0, -1):
       if x[0]%i ==0 and x[1]%i ==0:
           d = i
           break;
   total = 0
   for i in str(d):
       total += int(i)
   if total < 2: c = 0;
   else:
       for i in range (2,int(math.sqrt(total))+1):
           if total % i ==0 :
               c = 0
               break
   if c == 0: print("NO")
   else: print("YES")
   num -= 1




