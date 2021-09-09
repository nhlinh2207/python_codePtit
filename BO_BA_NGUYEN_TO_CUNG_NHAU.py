def USCLN_1(a, b):
    if b == 0:
        return a
    return USCLN_1(b, a % b)


vao = input()
tmp = vao.split()
a = int(tmp[0])
b = int(tmp[1])

for i in range(a, b-1):
    for j in range(i+1, b):
        if USCLN_1(i, j)==1:
           for k in range(j+1, b+1):
                if USCLN_1(k, j)==1 and USCLN_1(k, i)==1:
                   print("(%d, %d, %d)" %(i,j,k))