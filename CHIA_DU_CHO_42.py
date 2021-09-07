#x = [int(i) for i in input().split()]
list = []
while(True):
    x = [int(i) for i in input().split()]
    for i in x: list.append(i)
    if len(list) == 10:
        break

s = set({})
for i in list: s.add(i%42)
print(len(s))

