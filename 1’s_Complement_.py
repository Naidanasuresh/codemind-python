dec=int(input())
bi=0
temp=dec
i=0
while (temp!=0):
    bi=((temp%2)*(10**i)+bi)
    temp=int(temp/2)
    i=i+1
lst=str(bi)
st='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'
for i in lst:
    if i=='1':
        st+='0'
    else:
        st+='1'
by=int(st,2)
print(by)