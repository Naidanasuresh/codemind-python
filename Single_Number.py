n=int(input())
lst=list(map(int,input().split()))
res=0
for i in lst:
    res^=i
print(res)