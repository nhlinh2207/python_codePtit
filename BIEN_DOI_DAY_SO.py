ok=True
while ok==True:
    a=[int(i) for i in input().split()]
    if a[0]==0 and a[1]==0 and a[2]==0 and a[3]==0 :
        ok=False
    else:
        kt=False
        dem=0
        while kt==False:
            if a[0]==a[1]==a[2]==a[3]:
                kt=True
            else:
                k=a[0]
                a[0]=abs(a[0]-a[1])
                a[1]=abs(a[1]-a[2])
                a[2]=abs(a[2]-a[3])
                a[3]=abs( a[3]-k )
                dem+=1
        print(dem)