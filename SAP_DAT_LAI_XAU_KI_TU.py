num = int(input())
count = 1;
while num > 0:
    val1 = input()
    val2 = input()
    li1 = []
    li2 = []
    for i in val1:
        li1.append(i)
    for i in val2:
        li2.append(i)
    li1.sort()
    li2.sort()
    if(len(li1) != len(li2)):
        print("Test "+str(count)+": " +"NO")
    else:
        c = 0
        for i in range(0,len(li1)):
            if(li1[i] != li2[i]):
                c+=1
        if c == 0:
            print("Test "+str(count)+": " +"YES")
        else:
            print("Test "+str(count)+": " +"NO")
    count += 1
    num -=1