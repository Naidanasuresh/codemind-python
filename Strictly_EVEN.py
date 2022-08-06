n=int(input())
lst=list(map(int,input().split()))
cnt=0
c=[]
for i in range(len(lst)):
    if lst[i]%2==0 and i%2==0:
        cnt+=1
for i in lst:
    if i%2==0:
        c.append(i)
if cnt>=len(c):
    print(True)
else:
    print(False)