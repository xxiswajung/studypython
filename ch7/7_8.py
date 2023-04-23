n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
mid=n//2
sum=0
for i in range(mid):
    for j in range(mid-i,mid+i+1):
        sum+=arr[i][j]
        sum+=arr[n-i-1][j]
for i in range(n):
    sum+=arr[mid][i]
print(sum)

############################################
#BFS 이용

from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
ch=[[0]*n for _ in range(n)]
sum=0
Q=deque()
ch[n//2][n//2]=1
sum+=arr[n//2][n//2]
Q.append((n//2,n//2))
L=0 #level 0

while True: 
    if L==n//2:
        break
    size=len(Q)
    for i in range(size):
        tmp=Q.popleft()
        for j in range(4):
            x=tmp[0]+dx[j]
            y=tmp[1]+dy[j]
            if ch[x][y]==0:
                sum+=arr[x][y]
                ch[x][y]=1
                Q.append((x,y))
    L+=1
print(sum)
