n=int(input("enter a no"))
rev=0
while(n>0):
    r=int(n%10)
    rev=rev*10+r
    n=int(n/10)
print(rev)    

