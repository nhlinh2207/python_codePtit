x = input()
h = 0
t= 0
for i in x:
    if i.isupper():
        h += 1
    if i.islower():
        t +=1
if t >= h:
    print(x.lower())
else:
    print(x.upper())