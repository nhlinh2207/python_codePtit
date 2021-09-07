num = int(input())
while num > 0:
    val = input()
    list1 = []
    list2 = []
    c = 0;
    for i in range(1,len(val)):
       list1.append(abs(int(ord(val[i])) - int(ord(val[i-1]))))
    for i in range(len(val)-1,0,-1):
       list2.append(abs(int(ord(val[i])) - int(ord(val[i-1]))))

    for i in range(0,len(list1)):
       if list1[i] != list2[i]:
           c =1
    if c == 1:
      print("NO")
    else:
      print("YES")
    num -=1