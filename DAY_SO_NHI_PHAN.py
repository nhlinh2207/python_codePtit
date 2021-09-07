x = int(input())
y = [int(i) for i in input().split()]
c = 0
for i in range (0,len(y)-1):
    if(y[i] != y[i+1]):
        c+=1

print(c)


