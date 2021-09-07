def tich(list1):
    tich = 1
    for i in list1:
        tich*=int(i)
    return tich
x = int(input())
while x>0:
    num = int(input())
    list1 = [int(i) for i in input().split()]
    v = []
    for i in list1:
        v.append([tich(str(i)),i])
    v.sort()
    for i in range(len(v)):
        print(v[i][1],end=" ")
    print()
    x-=1