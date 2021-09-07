x = int(input())
while x>0:
    num = int(input())
    list1 = [int(i) for i in input().split()]
    list2 = [int(i) for i in input().split()]
    list2.sort()
    list1.sort()
    c = 0
    for i in range(num):
        if list1[i] >list2[i]:
            print("NO")
            c = 1;
            break;
    if c == 0:
        print("YES")
    x-=1