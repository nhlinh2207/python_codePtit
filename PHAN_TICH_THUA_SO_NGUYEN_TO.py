num = int(input())
while num > 0:
   res = "1"
   x = int(input()) #[int(i) for i in input().split()]
   c = dict({})
   while x%2 == 0:
       if 2 in c:
           c[2] += 1
       else:
           c.update({2:1})
       x = int(x/2)
   for i in range(3,x+1):
       while x%i ==0:
           if i in c:
               c[i] += 1
           else:
               c.update({i: 1})
           x = int(x/i)
   for i in c:
       temp = str(i)+"^"+str(c[i])
       res +=" * "+temp
   print(res)
   num -= 1



