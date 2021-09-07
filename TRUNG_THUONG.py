x = int(input())
while x>0:
    num = int(input())
    t = []
    while num > 0:
        t.append(int(input()))
        num-=1
    t.sort()
    curr = 1
    ma = 1;
    res = t[0]
    for i in range(1,len(t)):
        if(t[i-1] == t[i]):
            curr+=1
        else:
            if curr > ma:
                ma = curr
                res = t[i-1]
            curr = 1
    if curr > ma:
        ma = curr
        res = t[len(t)-1]
    print(res)
    x-=1