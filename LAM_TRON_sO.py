num = int(input())
while num>0:
    val = []
    list = input()
    for i in list:
        val.append(i)
    if len(val) == 1:
        val[0]
    else:
        for i in range (len(val)-1,0,-1):
            if int(val[i]) == 0:
                continue
            else:
                if int(val[i]) >= 5:
                    val[i-1] = str(int(val[i-1])+1)
                    for j in range(i,len(val)):
                        val[j] = str(0)
                else:
                    for j in range(i,len(val)):
                        val[j] = str(0)
    for i in val:
        print(i,end="")
    print()
    num -= 1
