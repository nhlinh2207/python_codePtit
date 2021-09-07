num = [int(i) for i in input().split()]
a = num[0]
k = num[1]
n = num[2]
if a>=n:
    print("-1")
else:
    c = 0
    mi = 0;
    if a==k:
        mi = a
    elif a>k:
        mi = k-a%k
    else:
        mi = k-a
    while mi<=(n-a):
        print(mi,end=" ")
        c+=1
        mi+=k
    print()
    if c==0:
        print("-1")