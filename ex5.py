#tính tổng 1^2+2^2+3^2+....+n^2
print("nhập n cần tính : ")
n=int(input())
s=0
i=1
for i in range(1,n+1):
    if i <= n:
        s=s+i**2
        i=i+1
print(f"tổng đến {n}^2 là",s)