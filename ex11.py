#đếm tất cả các ước số của số nguyên dương n
print("nhập số nguyên dương n")
n=int(input())
i=1
count = 0
for i in range(1,n+1):
    if i <= n:
        s = n%i
        if s == 0:
            count = count + 1
            i = i + 1
        else:
            i = i + 1
print(f"số nguyên dương {n} có {count} ước số")