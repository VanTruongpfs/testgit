#check xem n có phải là số nguyên tố hay không
print("nhập số nguyên dương n")
n=int(input())
i=1
count = 0
for i in range(1,n+1):
    if i<=n:
        s=n%i
        if s == 0:
            count = count + 1
            i = i + 1
        else:
            i = i + 1
if count == 2 :
    print(f"số {n} là số nguyên tố")
else:
    print(f"số {n} không phải là số nguyên tố")