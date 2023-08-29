#tính tổng các ước nguyên chẳn của số nguyên dương n
print("nhập số nguyên n")
n=int(input())
i=1
T=0
for i in range(1,n+1):
    if i <= n:
        s = n%i
        if s==0:
            if i%2 == 0:
                T=T+i
                i=i+1
        else:
            i=i+1
if T==0:
    print(f"số nguyên dương {n} không có ước nguyên chẳn nào")
else:
    print(f"tổng các ước nguyên chẳn của số nguyên dương {n} là:",T)
