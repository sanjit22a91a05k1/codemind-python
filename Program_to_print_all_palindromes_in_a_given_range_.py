def pal(n):
    t=n
    rev=0
    while(n!=0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if(rev==t):
        return 1
    else:
        return 0
n1=int(input())
n2=int(input())
for i in range(n1,n2+1):
    if(pal(i)):
        print(i, end=" ")
        