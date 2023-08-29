#tính tích tất cả các ước số của số nguyên dương n
print("nhập số nguyên n cần tính")
n=int(input())
i=1
T=1
for i in range(1,n+1):
    if i <= n:
        s=n%i
        if s == 0:
            T=T*i
            i=i+1
        else:
            i=i+1
print(f"tích các ước của số nguyên {n} là:",T)