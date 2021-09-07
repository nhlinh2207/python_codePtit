x = int(input())
y = [int(i) for i in input().split()]
y.sort()
if y[0]>1:
    print("1")
else:
    c = 0
    for i in range(1,len(y)):
        if(y[i]-y[i-1] >= 2):
            print(y[i-1]+1)
            c+=1
            break
    if c == 0:
        print(y[len(y)-1]+1)