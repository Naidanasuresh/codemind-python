n=int(input())
lst=list(map(int,input().split()))
x=0
for i in range(n):
    if lst[i]%2==0:
        x+=1
if x==n:
    print(True)
else:
    print(False)