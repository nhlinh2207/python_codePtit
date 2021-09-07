def chan(n):
    m=str(n)
    if len(m)%2==1:
        return False
    for i in range(len(m)):
        tmp=int(m[i])%2
        if tmp==1:
            return False
    return True

def STN(n):
    m=str(n)
    num=int(len(m)/2)
    for i in range(num):
        if m[i]!=m[len(m)-i-1]:
            return False
    return True


t = int(input())
while(t>0):
    n = int(input())
    ra=""
    for i in range(22, n, 22):
        if chan(i)==True and STN(i)==True:
            ra+=str(i)+" "
    print(ra)
    t-=1