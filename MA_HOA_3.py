t = int(input())
while t > 0:
    s = input()
    # chia
    s_1 = ''
    s_2 = ''
    for i in range(int(len(s) / 2)):
        s_1 += s[i]
    for i in range(int(len(s) / 2), len(s)):
        s_2 += s[i]

    # xoay
    sum1, sum2 = 0, 0
    for i in s_1:
        sum1 += ord(i) - 65  # 65 la 'A' trong bang ma Ascii
    for i in s_2:
        sum2 += ord(i) - 65
    rotate1 = sum1 % 26  # xoay het 1 vong la 26 buoc
    rotate2 = sum2 % 26

    s_11 = ''  # tao xau moi vi tung phan tu xau cu khong gan lai duoc gia tri khac(cac ptu nay deu la string)
    s_22 = ''

    for i in range(len(s_1)):
        res = ord(s_1[i]) + rotate1
        if res <= 90:
            s_11 += chr(res)
        else:
            res = res - 1 - 90 + 65
            s_11 += chr(res)

    for i in range(len(s_2)):
        res = ord(s_2[i]) + rotate2
        if res <= 90:
            s_22 += chr(res)
        else:
            res = res - 1 - 90 + 65
            s_22 += chr(res)

            # tron
    final_s = ''
    for i in range(len(s_11)):
        rotate = ord(s_22[i]) - 65
        res = ord(s_11[i]) + rotate
        if res <= 90:
            final_s += chr(res)
        else:
            res = res - 1 - 90 + 65
            final_s += chr(res)
    print(final_s)

    t -= 1