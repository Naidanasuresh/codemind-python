n=int(input())
lst=list(map(int,input().split()))
c=0
f=[]
for i in range(n):
    if lst[i]%2==0 and i%2==0:
        c+=1
for i in lst:
    if i%2==0:
        f.append(i)
if c>=len(f):
    print(True)
else:
    print(False)