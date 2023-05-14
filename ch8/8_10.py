n=int(input())
arr=list(map(int,input().split()))
m=int(input())
dy=[100]*(m+1)
dy[0]=0

for i in arr:
    for j in range(i,m+1):
        dy[j]=min(dy[j],dy[j-i]+1)
print(dy[m])
