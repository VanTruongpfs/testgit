#tính tổng x+x^2+x^3+....+x^n
print("nhập x và n cần tính tổng")
x=int(input())
n=int(input())
s=0
i=1
for i in range(1,n+1):
    if i <= n:
        s = s + x**i
        i = i + 1
print(f"tổng đến {x}^{n} của dãy là :",s)
        