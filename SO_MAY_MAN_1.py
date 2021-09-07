
#num = int(input())
#while num > 0:
x = input() #[int(i) for i in input().split()]
bon = 0
bay = 0
for i in x:
    if i == "4": bon += 1
    elif i == "7": bay += 1
if bay+bon == 7 or bay+bon == 4:
    print("YES")
else: print("NO")
   #num -= 1