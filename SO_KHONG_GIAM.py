num = int(input())
for i in range(num):
       a = input()
       c = 0
       for i in range(0,len(a)-1):
          if int(a[i]) > int(a[i+1]):
            c+=1
            break
       if c==0:
          print("YES")
       else: print("NO")