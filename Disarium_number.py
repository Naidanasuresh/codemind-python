n=int(input())
i=1
sum=0
t=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    
    n=n//10
while rev>0:
    m=rev%10

    k=m**i
    i+=1
    sum=sum+k
    rev=rev//10
if sum==t:
    print(True)
else:
    print(False)
