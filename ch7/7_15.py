from collections import deque

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(m)]
Q=deque()
for i in range(m):
    for j in range(n):
        if arr[i][j]==1:
            Q.append((i,j))
dx=[-1,0,1,0]
dy=[0,1,0,-1]
cnt=0

while Q:
    r=0
    for j in range(m):
        for k in range(n):
            if arr[j][k]==0:
                r+=1
    if r==0:
        break
    lth=len(Q)
    for _ in range(lth):
        res=Q.popleft()
        for i in range(4):
            x=res[0]+dx[i]
            y=res[1]+dy[i]
            if 0<=x<m and 0<=y<n and arr[x][y]==0:
                arr[x][y]=1
                Q.append((x,y))
    cnt+=1
for j in range(m):
    for k in range(n):
        if arr[j][k]==0:
            print(-1)
            sys.exit()
print(cnt)
