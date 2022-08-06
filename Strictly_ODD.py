n=int(input())
lst=list(map(int,input().split()))
f=0
c=[]
for i in range(n):
    if lst[i]%2==1 and i%2==1:
        f+=1
for i in lst:
    if  i%2==1:
        c.append(i)
if f>=len(c):
    print(True)
else:
    print(False)
        