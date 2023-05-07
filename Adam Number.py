n=int(input())
sq=n*n
rev=0;
while(n!=0):
    r=n%10
    rev=rev*10+r
    n=n//10

s=rev*rev;
re=0;
while(s!=0):
    rem=s%10
    re=re*10+rem
    s=s//10
if(sq==re):
    print("True")
else: 
       print("False");
   
