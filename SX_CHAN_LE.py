num = int(input())
list = []
while len(list) <num:
    val = [int(i) for i in input().split()]
    for i in val:
        list.append(i)
c1 = []
c2 = []
l1 = []
l2 = []
for i in range(0, len(list)):
    if list[i]%2 == 0:
        c1.append(i)
        c2.append(list[i])
    else:
        l1.append(i)
        l2.append(list[i])
c2.sort()
l2.sort()
l2.reverse()
res = []
for i in range(0,len(list)):
    res.append(0)
for i in range (0,len(c1)):
    res[c1[i]] = c2[i]
for i in range(0, len(l1)):
    res[l1[i]] = l2[i]
for i in res:
    print(i,end=" ")
print()
