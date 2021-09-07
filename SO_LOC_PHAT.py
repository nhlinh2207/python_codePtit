p = int(input())
for i in range(p):
    num = input()
    if num[len(num)-2] == "8" and num[len(num)-1]=="6":
        print("YES")
    else: print("NO")