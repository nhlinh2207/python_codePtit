def USCLN_1(a, b):
    if b == 0:
        return a
    return USCLN_1(b, a % b)
vao = input()
inp = vao.split()
N = int(inp[0])
K = int(inp[1])
ra=""
tmp = 0
for i in range(pow(10,K-1), pow(10, K)):
    if tmp!=0 and tmp%10==0:
        ra+="\n"
    if USCLN_1(i, N)==1:
        ra+=str(i)+" "
        tmp+=1
print(ra)