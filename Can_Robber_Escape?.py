n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if(a[i]>=n):
        c+=1
if(c==0):
    print("YES")
else:
    print("NO")
       