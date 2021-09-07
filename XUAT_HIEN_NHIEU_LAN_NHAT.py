x = int(input())
while x>0:
    num = int(input())
    list1 = [int(i) for i in input().split()]
    maxcount = 1
    list1.sort()
    res = list1[0]
    curr = 1
    for i in range(1, len(list1)):
        if list1[i] == list1[i-1]:
            curr+=1
        else:
            if(curr > maxcount):
                maxcount = curr
                res = list1[i-1]
            curr = 1
    if (curr > maxcount):
        maxcount = curr
        res = list1[len(list1) - 1]

    if(maxcount > len(list1)/2):
        print(str(res))
    else:
        print("NO")
    x-=1