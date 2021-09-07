def check(sum):
    if len(str(sum)) == 1:
        return "NO"
    else:
        list1 =[]
        for i in str(sum):
            list1.append(i)
        list2 = []
        for i in range(len(str(sum)) -1,-1,-1):
            list2.append(str(sum)[i])
        for i in range(0,len(list1)):
            if list2[i] != list1[i]:
                return "NO"
        return "YES"
n = int(input())
while n>0:
    num = input();
    sum = 0
    for i in num:
        sum+=int(i)
    print(check(sum))
    n-=1