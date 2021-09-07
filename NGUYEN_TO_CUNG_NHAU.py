def check(a,b):
    while a!=b:
        if a<b :
            b-=a
        else:
            a-=b
    if a==1:
        return 1
    else:
        return 0
x = input()
list = [int(i) for i in input().split()]
list.sort()
for i in range(0,len(list)-1):
    for j in range(i+1,len(list)):
        if(check(list[i], list[j]) == 1):
            print(str(list[i])+" "+str(list[j]))
