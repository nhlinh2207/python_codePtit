x = int(input())
while(x>0):
    y = input()
    num = []
    for i in y:
        num.append(int(i))
    t = num[0]
    c = 0
    for i in range(1,len(num)):
        if abs(num[i] - num[i-1]) != 2:
            c += 1
            break
        else: t = t+num[i]
    if c == 0 and t%10 == 0: print("YES")
    else: print("NO")
    x -= 1