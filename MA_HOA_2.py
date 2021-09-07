list1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","_","."]
while(True):
    val = input()
    if val == "0":
        break
    gtri = val.split()
    k = int(gtri[0])
    chuoi = gtri[1]
    res = ""
    for i in range(0,len(chuoi)):
        index = list1.index(chuoi[i])
        j = k+index
        if(j > 27):
            j = j-27-1
        res += list1[j]
    print(res[::-1])
