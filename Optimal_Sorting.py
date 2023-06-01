t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    b=max(a)
    c=min(a)
    d=sorted(a)
    if(d==a):
        print("0")
    else:
        print(b-c)
    