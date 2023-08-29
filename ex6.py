#tính tổng 1/2+1/3+1/4+...+1/n
print("nhập số n cần tính:")
n=int(input())
s=0
i=2
for i in range(2,n+1):
    if i <= n:
        s=s+1/i
        i=i+1
print(f"tổng đến 1/{n} tính =",s)