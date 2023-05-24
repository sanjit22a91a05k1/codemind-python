t=int(input())
f=0
v=0
for i in range(t):
   
    n,a,b,k=map(int,input().split())
    c1=n//a;
    c2=n//b;
    c3=n//(a*b)
    if(c1+c2-c2>=k):
        print("Win")
    else:
        print("Lose");
    
    


    
    