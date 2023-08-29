#tính tổng giá trị 1+1+2+1+2+3+...+n
print("nhập giá trị n:")
n=int(input())
s=0
i=1
for i in range(1,n+1):
    if i<=n :
        s = s + i
        i = i + 1
print("tổng giá trị là:",s)   