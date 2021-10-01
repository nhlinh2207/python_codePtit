start, end, cso = input().split()
start, end, cso = int(start), int(end), int(cso)

List_num = [0,1,3,5,7] #la cac so dxung dau tien 0,1,11, 101, 111

key = ['', '0', '1']
arr = []

def genbin(n, bs=''):
    if len(bs) == n:
        for i in range(len(key)):
            tmp = '1' + bs
            tmp = list(tmp)
            tmp.reverse()
            tmp = ''.join(tmp)
            res =  '1' + bs + key[i] + tmp
            if len(res) == 21:
                if chuyennhiphan(res) <= 2000000:
                    arr.append(chuyennhiphan(res))
            else:
                arr.append(chuyennhiphan(res))
    else:
        genbin(n, bs + '0')
        genbin(n, bs + '1')

def chuyennhiphan(num):
    dem = 0
    sum = 0
    for i in range(len(num)-1,-1,-1):
        sum += int(num[i])*2**dem
        dem+=1
    return sum


for i in range(1,10):
    arr.clear()
    genbin(i)
    List_num.extend(arr)

List_num.sort()



def chuyencso(num, cso):
    res = []
    while num!=0:
        res.append(num%cso)
        num = int(num/cso)
    res.reverse()
    res = ''.join([str(i) for i in res])
    return res

def check(num):
    for i in range(len(num)//2):
        if num[i] != num[len(num)-1-i]:
            return False
    return True


count = 0
for num in List_num:
    if num > end:
        break
    elif num < start:
        continue
    else:
        check_num = True
        for cs in range(2, cso+1):
            if check(chuyencso(num,cs))==False:
                check_num = False
                break
        if check_num:
            count += 1
print(count)