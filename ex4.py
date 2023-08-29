#tính tổng 1!+2!+3!+...+n!
print("nhập giá trị n :")
n=int(input())
T = 1
s = 0
i = 1
for i in range(1,n+1):
    if i <= n :
        T = T * i
        s = s + T
        i = i + 1
print(f"tổng là:{s}")