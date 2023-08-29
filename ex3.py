# tính 1x2x3x4x5x6...xn
print("nhập số hạng cần n tính :")
n = int(input())
s = 1
i = 1
for i in range(1,n+1):
    if i <= n:
        s = s*i
        i = i + 1
print (n ,"giai thừa =",s)