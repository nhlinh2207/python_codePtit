num = int(input())
x = [int(i) for i in input().split()]
c = 0
for i in range(0,len(x)-1):
    for j in range(i+1, len(x)):
        if x[i] > x[j]:
            c += 1
print(c)
