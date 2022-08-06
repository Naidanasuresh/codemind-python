S,T,B=map(int,input().split())
cap=2*S*T*B*512
c=cap//1024
print(c,end='KB')