t = int(input())
c=list()
for i in range(t):
    n,s,e,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=a[s-1:e]
    b.sort()
    c.append(b[k-1])

for j in range(t):
    print("#%d %d" %(j+1,c[j]))
