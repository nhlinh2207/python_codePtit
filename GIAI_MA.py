p = int(input())
for i in range(p):
    num = input()
    res = ""
    for i in range(0,len(num),2):
        t = num[i]*int(num[i+1])
        res += t
    print(res)