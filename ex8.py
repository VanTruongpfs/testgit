#liệt kê tất cả các ước nguyên dương của số n
print("nhập số n cần liệt kê")
n=int(input())
i=1
for i in range(1,n+1):
    if i <= n:
       if n%i == 0:
           print (i)
           i=i+1
       else :
           i=i+1