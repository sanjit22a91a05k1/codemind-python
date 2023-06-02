n=int(input())
t=n
s=0
while(n!=0):
    fac=1
    r=n%10
    for i in range(1, r+1):
        fac=fac*i
    s=s+fac
    n=n//10
if(s==t):
    print("The number %d is a strong number"%t)
else:
     print("The number %d is not a strong number"%t)
    
    