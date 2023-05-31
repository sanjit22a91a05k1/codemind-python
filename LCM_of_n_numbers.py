n=int(input())
a=list(map(int, input().split()))
b=max(a)
for j in range(b,100000):
    c=0
    for i in range(0,n):
        if(j%a[i]==0):
            c+=1
    if(c==n):
        print(j)
        break
