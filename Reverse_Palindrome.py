def palindrome(n):
    rev=0
    while(n!=0):
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev


n=int(input())
n=n+palindrome(n)
while(n!=palindrome(n)):
    n=n+palindrome(n)
print(n)