
num = int(input())
matran = []
sum = 0
nuatren = 0
cheophu = 0
while num > 0:
    row = [int(i) for i in input().split()]
    matran.append(row)
    num -=1 ;
balance = int(input())
for i in range(0,len(matran)):
    for j in range(0,len(matran[i])):
        sum+=matran[i][j]
        if j < len(matran[i]) - i- 1:
            nuatren += matran[i][j]
        if j == len(matran[i]) - i- 1:
            cheophu += matran[i][j]
nuaduoi = sum - cheophu - nuatren
if abs(nuaduoi - nuatren) <= balance:
    print("YES")
else:
    print("NO")
print(abs(nuaduoi - nuatren))

