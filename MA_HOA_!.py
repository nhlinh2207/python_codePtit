x = int(input())
while x>0:
    num = input()
    #list1 = [int(i) for i in input().split()]
    curr = 1
    res = ""
    for i in range(1,len(num)):
        if num[i] == num[i-1]:
            curr+=1
        else:
            res+=str(curr)+num[i-1]
            curr = 1
    if curr > 1:
        res+=str(curr)+num[len(num) -1]
    if curr == 1:
        res+=str(curr)+num[len(num) - 1]
    print(res)
    x-=1