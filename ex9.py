#tính tổng các ước nguyên của số nguyên dương n
print("nhập số nguyên dương n cần tính")
n=int(input())
i=1
T=0
for i in range(1,n+1):
    if i <= n:
        s=n%i
        if s==0:
            T=T+i
            i=i+1    
        else:
            i=i+1
print(f"tổng các ước của số {n} là:",T)