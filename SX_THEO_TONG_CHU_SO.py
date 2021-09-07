def sum(list1):
    tong = 0
    for i in list1:
        tong+=int(i)
    return tong
x = int(input())
while x>0:
    num = int(input())
    list1 = [int(i) for i in input().split()]
    v = []
    for i in list1:
        v.append([sum(str(i)),i])
    v.sort()
    for i in range(len(v)):
        print(v[i][1],end=" ")
    print()
    x-=1