
num = int(input())
val = [float(i) for i in input().split()]
mi = min(val)
ma = max(val)
c = 0
sum = 0
for i in val:
    if i!=mi and i!=ma:
        sum+=i
        c+=1
print("{:.2f}".format(sum/c))