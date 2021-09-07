
num = int(input())
while num > 0:
   x = input() #[int(i) for i in input().split()]
   c = 1;
   for i in x:
       if(i != "7" and i != "4"):
           c = 0
           break
   if c == 0: print("NO")
   else: print("YES")
   num -= 1