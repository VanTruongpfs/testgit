#liệt kê tất cả ước số nguyên dương lẻ cửa số nguyên dương n
print("nhập số nguyên dương n")
n=int(input())
print(f"các số ước nguyên lẻ của {n} là:")
i=1
for i in range(1,n+1):
    if i <= n :
        s = n%i
        if s == 0:
            if i%2!=0:
                print(i)
                i=i+1
            else:
                print(f"số {n} không có số ước nguyên lẻ nào")#usually có 1 ước nguyên lẻ is number 1, so this case can't happen
        else:
            i=i+1
