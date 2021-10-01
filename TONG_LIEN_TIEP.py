# Ý tưởng:
# Nhận thấy tổng liên tục từ x đến y kqua la (y-x+1)(x+y)/2 = n nên (y-x+1)*(x+y) = 2n 
# do đó ta kiểm tra các số là ước của 2n nhưng phải chú ý là y-x+1 và x+y khác tính chẵn lẻ và y-x+1< x+y. 
# Bài toán đưa về đếm số cặp x.y=2n mà x và y khác tính chẵn lẻ và x<y do đó duyệt từ 1 đến căn 2n là xong
from math import *
t = int(input())

def dem_uoc(a):
    num = a*2
    count = 0
    k = int(sqrt(num))
    for i in range(2, k+1):
        if num % i == 0:
            x = num / i
            if (x - i) % 2 != 0: # kiemm tra 2 so thoa man dkien khac nhau chan le khong
                count += 1
    return count


while t > 0:
    n = int(input())
    print(dem_uoc(n))
    t-=1