#x = [int(i) for i in input().split()]
while(True):
    x = int(input())
    if x != 0 :
       list = []
       list.append(x)
       while(x != 1):
          if x%2 == 0:
              x /= 2
              list.append(x)
          else:
              x = x*3+1
              list.append(x)
       print(len(list))
    else: break