#tìm ước nguyên lẻ lớn nhất của số nguyên dương n
print("nhập số nguyên dương n")
n=int(input())
i=1
dv=0
for i in range(1,n+1):
    if i <= n:
        s = n%i
        if s == 0 and i%2 != 0:
            dv=i
            i=i+1
        else:
            i=i+1
print(dv)